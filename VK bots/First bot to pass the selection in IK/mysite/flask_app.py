# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
import vk_api
import random
import traceback
import requests
import datetime
import calendar
import main_keyboards


DEV_ID = 189583025
vk = vk_api.VkApi(token = 'vk1.a.0BS2yJtt5O0QtlnwYXmw6Fk_AdUQXdb7atLoqsUbgPR5BOg5XdRY7EBUyVVbVP8j7DlDGh70rNJO_WShfuzSph4lLHeS1DxFoUOIznJbfP68o_shH43vi8Px98i0w9apOyAl_9LO_v-R46JqLKD19UqXYvR1qh8rlTJP-vzaCxw4CNBKOdq4rTa68109ABlI')
max_sudents = 1

#Уведомляет разработчика об ошибке в файле с контентом
def content_error_message(id, error_type):
    vk.method("messages.send", {"peer_id" : id,
                                "message" : "Извините, в данный момент информация недоступна. Попробуйте позже",
                                "keyboard" : main_keyboard,
                                "random_id" : random.randint(1, 2147483647)})
    error_type = "Отсутствует файл с данными по теме.\n" + error_type + "\nНужно исправить!"
    vk.method("messages.send", {"peer_id" : DEV_ID,
                                "message" : error_type,
                                "random_id" : random.randint(1, 2147483647)})
#Проверяет сцществование файла
def try_file_reading(file_name):
    data_request = []
    try:
        with open(file_name,'r', encoding="utf-8") as read_file:
            data_request = json.load(read_file)
            read_file.close()
    except FileNotFoundError:
        data_request = []
    return data_request

#Открывает фото и получает данные для того, чтобы отправить его как attachement
def upload_photo(upload, img):

    response = upload.photo_messages(img)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key

#Отправляет фото по параметрам из upload_photo
def send_photo(peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.method("messages.send", {"random_id" : random.randint(1, 2147483647),
                                "peer_id" : peer_id,
                                "attachment" : attachment})

#Создаёт файл с расписанием вебинаров. Кнопки не отсортированы по дню недели и пока не обновляются в конце недели.
def create_timetable():
    dict = {}
    week_days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    lesson_time = ["11:00", "17:00"]
    for i in week_days:
        for j in lesson_time:
            dict[i + j] = []

    with open('web_time.json','w', encoding = "utf-8") as write_file:
        json.dump(dict, write_file)
    write_file.close()




#Клавиатуры для этого бота

#Основная клавиатура
main_keyboard = main_keyboards.main_keyboard_menu.get_keyboard()

#Клавиатура общежитий
dorm_keyboard = main_keyboards.dorm_keyboard_menu.get_keyboard()

#Пустая клавиатура
empty_keyboard = vk_api.VkKeyboard().get_empty_keyboard()

#Клавиатура для возврата к первоначальному меню
reset_keyboard_menu = vk_api.VkKeyboard(one_time=False)
reset_keyboard_menu.add_button("Вернуться", "negative", {"type" : "return"})

#Пожелания от бота
texts = ["Хорошего дня, ", "Удачи на сессии, ", "Учти, 'Я робот' уже не настолько фантастика, ", "Погода сегодня отличная для прогулки, "]
person = ["Господин.", "человечек", "пользователь", "но не тебе"]

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def start_work():
    try:
        data = json.loads(request.data)
        #Первое подключение и подтверждение
        if data["type"] == "confirmation":
           return "e6193f18"

        elif data["type"] == "message_new":

            #Сохранение данных собеседника
            obj = data["object"]["message"]
            id = obj["peer_id"]
            body = obj["text"]

            #Проверка наличия payload сообщений
            try:
                payload = eval(obj["payload"])
            except KeyError:
                payload = None

            ######Проверка повторяющихся сообщений
            log = try_file_reading("log.json")

            if data['event_id'] in log:
                return "ok"

            log.append(data['event_id'])

            with open('log.json','w') as write_file:
                json.dump(log, write_file)
            write_file.close()

            ##################################################################   Все команды для бота

            #Тестовая команда - хотим получить айди беседы
            if body.lower() == "!айди":
                vk.method("messages.send", {"peer_id" : id,
                                            "message" : id,
                                            "random_id" : random.randint(1, 2147483647)})
            elif body.lower() == "!меню":
                #Вызов клавиатуры
                vk.method("messages.send", {"peer_id" : id,
                                            "message" : "Пожалуйста, выберите нужный раздел",
                                            "keyboard" : main_keyboard,
                                            "random_id" : random.randint(1, 2147483647)})
            elif body.lower() == "!напутствие":
                message = random.choice(texts) + random.choice(person)
                vk.method("messages.send", {"peer_id" : id,
                                            "message" : message,
                                            "random_id" : random.randint(1, 2147483647)})
            elif body.lower() == "!помощь":
                #Список доступных команд
                vk.method("messages.send", {"peer_id" : id,
                                            "message" : "Вот список доступных команд\n\n!айди - возвращает id чата\n!меню - основная клавиатура с доступными командами\n!напутствие - желает всего наилучшего (или наихудшего)",
                                            "random_id" : random.randint(1, 2147483647)})
            #Проверяем, была ли нажата какая-то кнопка.  Соблюдаем иерархическую структуру клавиатур
            #Ключ словаря "type" проверяет, какая кнопка на ОСНОВНОЙ клавиатуре была нажата (сохранённая в payload) была нажата)
            elif payload != None:
                if payload["type"] == "contacts":
                    #Проверка на существование файла контактов
                    cont_data = try_file_reading("cont_data.json")
                    if len(cont_data) == 0:
                        content_error_message(id, "Контакты")
                    else:
                        vk.method("messages.send", {"peer_id" : id,
                                                    "message" : cont_data,
                                                    "random_id" : random.randint(1, 2147483647)})

                elif payload["type"] == "dorm":
                    #Переход с основной клавиатуры на клавиатуру общежитий
                    if (len(payload) == 1):
                        vk.method("messages.send", {"peer_id" : id,
                                                    "message" : "Выберите интересующее Вас общежитие",
                                                    "keyboard" : dorm_keyboard,
                                                    "random_id" : random.randint(1, 2147483647)})
                    #Работа с определённым общежитием
                    else:
                        #Проверка на существование файла общежитий
                        dorm_data = try_file_reading("dorm_data.json")

                        if len(dorm_data) == 0:
                            content_error_message(id, "Общежитие")
                        else:
                            #Проверяем, есть ли запрошенные данные
                            if payload["dorm"] not in dorm_data and payload["dorm"] != "back" and payload["dorm"] != "cost":
                                content_error_message(id, "Общежитие." + payload["dorm"])
                            else:
                            #Выводим информацию о запрошеном общежитии
                                if payload["dorm"] != "back" and payload["dorm"] != "cost":
                                    vk.method("messages.send", {"peer_id" : id,
                                                                "message" : dorm_data[payload["dorm"]],
                                                                "random_id" : random.randint(1, 2147483647)})
                                elif payload["dorm"] == "cost":
                                    vk_session = vk.get_api()
                                    upload = vk_api.upload.VkUpload(vk_session)
                                    send_photo(id, *upload_photo(upload, "dorm_cost.jpg"))
                                else:
                                    vk.method("messages.send", {"peer_id" : id,
                                                                "keyboard" : main_keyboard,
                                                                "message" : "Пожалуйста, выберите нужный раздел",
                                                                "random_id" : random.randint(1, 2147483647)})

                elif payload["type"] == "transport":
                    #Проверка на существование файла метрополитена
                    transport_data = try_file_reading("transport_data.json")
                    if len(transport_data) == 0:
                        content_error_message(id, "Метрополитен")
                    else:
                        vk.method("messages.send", {"peer_id" : id,
                                                    "message" : transport_data,
                                                    "random_id" : random.randint(1, 2147483647)})
                elif payload["type"] == "smile":

                    #Проверка на существование файла с ссылками на картинки. Тут должна быть нормальная работа с картинками, но её нет(
                    i = random.randint(1, 4)
                    images = try_file_reading("mem_images.json")
                    if len(images) == 0:
                        content_error_message(id, "мемЫ")
                    else:
                        vk_session = vk.get_api()
                        upload = vk_api.upload.VkUpload(vk_session)
                        send_photo(id, *upload_photo(upload, f"mem{i}.jpg"))

                        #vk.method("messages.send", {"random_id" : random.randint(1, 2147483647),
                         #   "peer_id" : id,
                          #  "attachment" : images[0]})

                elif payload["type"] == "web":
                    #Переход с основной клавиатуры на клавиатуру записи на вебинар
                    #Проверка на существование файла общежитий
                    #С помощью этой функции можно пересоздать расписание
                    #create_timetable()
                    schedule = try_file_reading("web_time.json")

                    if len(schedule) == 0:
                        content_error_message(id, "Вебинары")
                        return

                    #Клавиатура с доступными занятиями
                    web_time_menu = vk_api.VkKeyboard(one_time=False)
                    counter = 0
                    for i in schedule:
                        if len(schedule[i]) < max_sudents:
                            web_time_menu.add_button("Вебинар " + i, "primary", {"type" : "web", "web" : i})
                            counter += 1
                        if counter == 2:
                            web_time_menu.add_line()
                            counter = 0
                    if counter % 2 == 1:
                        web_time_menu.add_line()
                    web_time_menu.add_button("Показать свои занятия", "positive", {"type" : "web", "web" : "show"})
                    web_time_menu.add_line()
                    web_time_menu.add_button("Вернуться", "negative", {"type" : "web", "web" : "back"})
                    web_time = web_time_menu.get_keyboard()

                    #Нажатие на кнопку - Запись на вебинар
                    if (len(payload) == 1):
                        vk.method("messages.send", {"peer_id" : id,
                                                    "message" : "Выберите время, на которое хотите записаться",
                                                    "keyboard" : web_time,
                                                    "random_id" : random.randint(1, 2147483647)})
                    #Работа с временем и запись
                    else:
                        #Проверяем, есть ли запрошенные данные
                        if payload["web"] not in schedule and payload["web"] != "back" and payload["web"] != "show":
                            content_error_message(id, "Вебинар." + payload["web"])
                        else:
                            #Проверяем, куда студент записан
                            visited = []
                            for i in schedule:
                                for j in schedule[i]:
                                    if j == id:
                                        visited.append(i)
                            #Нажата кнопка записаться
                            if payload["web"] != "back" and payload["web"] != "show":

                                if len(schedule[payload["web"]]) < max_sudents and payload["web"] not in visited:
                                    schedule[payload["web"]].append(id)
                                    vk.method("messages.send", {"peer_id" : id,
                                                                "keyboard" : main_keyboard,
                                                                "message" : "Вы успешно записаны на занятие",
                                                                "random_id" : random.randint(1, 2147483647)})
                                elif payload["web"] in visited:
                                    vk.method("messages.send", {"peer_id" : id,
                                                                "keyboard" : web_time,
                                                                "message" : "Вы уже записаны на это занятие",
                                                                "random_id" : random.randint(1, 2147483647)})
                            #Нажата кнопка посмотреть имеющиеся занятия
                            elif payload["web"] == "show":
                                #Клавиатура с занятиями конкретного студента
                                if "show" not in payload.keys():
                                    your_web_menu = vk_api.VkKeyboard(one_time=False)
                                    counter = 0
                                    for i in visited:
                                        your_web_menu.add_button("Вебинар " + i, "primary", {"type" : "web", "web" : "show", "show" : i})
                                        counter += 1
                                        if counter == 2:
                                            your_web_menu.add_line()
                                            counter = 0
                                    if counter % 2 == 1:
                                        your_web_menu.add_line()
                                    your_web_menu.add_button("Назад.", "negative", {"type" : "web", "web" : "show", "show" : "back"})
                                    your_web = your_web_menu.get_keyboard()

                                    if len(visited) != 0:
                                        vk.method("messages.send", {"peer_id" : id,
                                                                    "keyboard" : your_web,
                                                                    "message" : "Вы записаны на следующие занятия. \nЕсли вы хотите отменить запись - нажмите на соответствующую кнопку.",
                                                                    "random_id" : random.randint(1, 2147483647)})
                                    else:
                                        vk.method("messages.send", {"peer_id" : id,
                                                                    "keyboard" : your_web,
                                                                    "message" : "Вы ещё не записаны ни на одно занятие.",
                                                                    "random_id" : random.randint(1, 2147483647)})
                                elif payload["show"] != "back":
                                    new_students = []
                                    for i in schedule[payload["show"]]:
                                        if i != id:
                                            new_students.append(i)
                                    schedule[payload["show"]] = new_students
                                    vk.method("messages.send", {"peer_id" : id,
                                                                "keyboard" : main_keyboard,
                                                                "message" : "Запись успешно удалена",
                                                                "random_id" : random.randint(1, 2147483647)})
                                elif payload["show"] == "back":
                                    vk.method("messages.send", {"peer_id" : id,
                                                                "keyboard" : web_time,
                                                                "message" : "Выберите интересующий Вас вебинар",
                                                                "random_id" : random.randint(1, 2147483647)})

                            #Вернуться назад
                            else:
                                vk.method("messages.send", {"peer_id" : id,
                                                            "keyboard" : main_keyboard,
                                                            "message" : "Пожалуйста, выберите нужный раздел",
                                                            "random_id" : random.randint(1, 2147483647)})
                            #Переносим новые данные о занятиях в файл
                            with open('web_time.json','w', encoding = "utf-8") as write_file:
                                json.dump(schedule, write_file)
                            write_file.close()

                elif payload["type"] == "work_end":
                    vk.method("messages.send", {"peer_id" : id,
                                                "message" : "Обращайтесь ещё)",
                                                "keyboard" : empty_keyboard,
                                                "random_id" : random.randint(1, 2147483647)})

    except :
        # Сообщение админу об ошибке
        vk.method("messages.send", {"peer_id" : DEV_ID,
                                    "message" : (traceback.format_exc()+'\n\n'+str(data))[:4096],
                                    "random_id" : random.randint(1, 2147483647)})
    return "ok"



