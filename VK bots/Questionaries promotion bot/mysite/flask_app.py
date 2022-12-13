
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
import vk_api
import traceback
import random
import csv
import datetime as dt
import validators
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

DEV_ID_SLAVA = 189583025
DEV_ID_IANA = 333624601
permited_id = [DEV_ID_SLAVA, DEV_ID_IANA]

vk = vk_api.VkApi(token = '4a1ad9b2bc44751e5c64c3e47fd433d5bec17ad9fdf8327daac702d648c1cf4690431ebac1b0c88710859')

####кнопка "добавить анкету"
key=VkKeyboard(one_time=False)
key.add_button('назад', color=VkKeyboardColor.NEGATIVE)
key.add_button('в анкете нет кода', color=VkKeyboardColor.NEGATIVE)

key1=VkKeyboard(one_time=True)
key1.add_button('Добавить анкету', color="positive")
key1.add_button('Просто пройти анкеты', color="positive")

key2=VkKeyboard(one_time=True)
key2.add_button('Подтвердить', color=VkKeyboardColor.PRIMARY)
key2.add_line()
key2.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

work_continue=VkKeyboard(one_time=True)
work_continue.add_button('Да', color=VkKeyboardColor.PRIMARY, payload = {"answer":"Yes"})
work_continue.add_button('Нет', color=VkKeyboardColor.NEGATIVE, payload = {"answer":"No"})


####Проверяет сцществование файла
def try_file_reading(file_name):
    data_request = []
    try:
        with open(file_name,'r', encoding="utf-8") as read_file:
            data_request = json.load(read_file)
            read_file.close()
    except FileNotFoundError:
        data_request = []
    return data_request

def check_url(user_url):
    res = validators.url(user_url)
    if res == True:
        return True
    return False

def check_code(code, id):
    j=list()
    with open('prob.csv','r', encoding="utf-8") as baza:
        reading = csv.reader(baza, delimiter=';')
        for row in reading:
            j.append(row[0])
    baza.close()
    fin_quests = try_file_reading("filled_quests.json")

    for i in j:
        if i.split(",")[5] == code:
            if i.split(",")[1] + ":" + str(id) in fin_quests:
                return 1
            else:
                return 0
    return -1



app = Flask(__name__)
@app.route('/', methods = ["POST"])
def start_work():
    try:
        data = json.loads(request.data)
####Первое подключение и подтверждение
        if data["type"] == "confirmation":
           return "514ba40a"
        elif data["type"] == "message_new":

####Сохранение данных собеседника
            obj = data["object"]["message"]
            id = obj["peer_id"]
            body = obj["text"]
            if body.lower() == "!инфа":
                vk.method("messages.send", {"peer_id": id, "message": id, "random_id": random.randint(2, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": dt.date.today(), "random_id": random.randint(2, 2147483647)})

####Проверка наличия payload сообщений
            try:
                payload = eval(obj["payload"])
            except KeyError:
                payload = None

 ####Проверка повторяющихся сообщений
            log = try_file_reading("log.json")

            if data['event_id'] in log:
                return "ok"


            log.append(data['event_id'])

            with open('log.json','w') as write_file:
                json.dump(log, write_file)
            write_file.close()

    ###Основа
        ##Открытие БД
            j=list()
            with open('prob.csv','r', encoding="utf-8") as baza:
                reading = csv.reader(baza, delimiter=';')
                for row in reading:
                    j.append(row[0])
            baza.close()
        ##Cписки для использования

            # j-список БД
            id_a = []  # name-список названий анкет
            ssl = []   # ssl-список ссылок
            nado = []  # nado-список необходимого кол-ва прохождений
            ddl = []   # ddl-список ддл
            cou = []   # cou-список кол-ва прохождений
            cod = []   # cod-список кодов подтверждения анкеты
            fin_quests = try_file_reading("filled_quests.json")

            j_new =[]
            fl = False

            for i in range(len(j)):
                cur_que = (j[i]).split(',')
                #Форматируем дату
                t = cur_que[3]
                t = t.replace("'", "")
                t = t.replace('"', '')
                t = dt.date(int(t[0:4]), int(t[5:7]), int(t[8:10]))

                #Проверка, прошёл ли дедлайн
                if t < dt.date.today():
                    fl = True
                    if cur_que[1] + ":" + str(id) in fin_quests:
                        del fin_quests[cur_que[1] + ":" + str(id)]
                else:
                    ###Отсев анкет, по которым прошёл дедлайн. j_new - новая версия базы
                    j_new.append([cur_que[0], cur_que[1], cur_que[2], t, int(cur_que[4]), cur_que[5]])
                    ###Смотрим, отвечал ли этот человек на эту анкету ранеее
                    if cur_que[1] + ":" + str(id) not in fin_quests:
                        id_a.append(cur_que[0])
                        ssl.append(cur_que[1])
                        nado.append(cur_que[2])
                        ddl.append(t)
                        cou.append(int(cur_que[4]))
                        cod.append(cur_que[5])

            ####Проверка - человек заполнил все анкеты
            if len(ssl) == 0 and body.lower() == "просто пройти анкеты":
                vk.method("messages.send", {"peer_id": id, "message": "Вы заполнили все анкеты.", "random_id": random.randint(2, 2147483647)})
                return "ok"
            if len(ssl) == 0 and body.lower() == "добавить анкету":
                vk.method("messages.send", {"peer_id": id, "message": "Вы заполнили все анкеты. \nК сожалению, мы не можем добавить вашу анкету", "random_id": random.randint(2, 2147483647)})
                return "ok"

            #Проверка. желает ли пользователь продолжить работу
            if payload != None and "answer" in payload:
                count_code = try_file_reading("count_code.json") #файл с кодами отправленными пользователями
                reply = ["Пришлите ссылку на анкету",
                        "Введите желаемое число заполнений",
                        "Введите крайний срок заполнения анкеты в формате гггг-мм-дд",
                        "Введите текущее количество заполнивших (или 0, если таких нет)"
                        ]
                payload = payload["answer"]

                if payload == "Yes":
                    count_code[str(id) + "P&D"] = "D"
                    count_code[str(id)]["finished"] = True
                    vk.method("messages.send", {"peer_id": id, "message":"Вот на чём Вы остановились:\n"+reply[int(count_code[str(id)]["status"])], "random_id": random.randint(2, 2147483647)})

                elif payload == "No":
                    del count_code[str(id) + "_create"]
                    count_code[str(id)]=dict()

                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
                if payload == "No":
                    body = "добавить анкету"
                if payload == "Yes":
                    return"ok"

        ###Начало
            glob_flag = 0
            if body.lower()=='начать':
                vk.method("messages.send", {"peer_id": id, "message":"Выберите что хотие сделать", "keyboard": key1.get_keyboard(), "random_id": random.randint(2, 2147483647)})
                dict_code=dict()
                count_code=dict()
                count_code = try_file_reading("count_code.json") #файл с кодами отправленными пользователями
                count_code_keys=count_code.keys()
                if str(id) in count_code_keys:
                    dict_code=count_code[str(id)]
                count_code[str(id)]=dict_code
                count_code[str(id)+'P&D']='0'
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
        ##Добавить анкету
            if  body.lower() == "добавить анкету":
                count_code=dict()
                dict_code=dict()
                count_code = try_file_reading("count_code.json") #файл с кодами отправленными пользователями
                if str(id) + "_create" in count_code:
                    vk.method("messages.send", {"peer_id": id, "message":"Вы уже начали добавлять анкету. Хотите продолжить?", "keyboard": work_continue.get_keyboard(), "random_id": random.randint(2, 2147483647)})
                    return"ok"

                count_code_keys=count_code.keys()
                if str(id) in count_code_keys:
                    dict_code=count_code[str(id)]
                count_code[str(id)+'P&D']='D'
                count_code[str(id)]=dict_code
                count_code[str(id)]["finished"] = False
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
                ##Отправка до 3 анкет. Поиск 3 анкет с наименьшим числом заполнивших её людей среди анкет, которые не заполнял конкретный пользователь.
                ind=[]
                indexx=[]
                for i in range(len(cou)):
                    indexx.append(i)
                dict_min1=dict(zip(indexx, cou))
                list_min=list(dict_min1.items())
                (list_min).sort(key=lambda i:i[1])
                dict_min=dict()
                for i in list_min:
                    dict_min[i[0]]=i[1]
                ind=list(dict_min.keys())[:3]

                ##(отправить анкеты)
                ####Отправка сообщений по анкетам
                anketa_str=''
                for i in ind:
                    anketa_str+=ssl[i]+'\n'

                anketa_str+='\nВот список актуальных анкет. \nКак пройдёте одну из них, пришлите, пожалуйста, код, который находиться в конце анкеты, он имеет вид: \nF-***'
                vk.method("messages.send", {"peer_id": id, "message": anketa_str + "\nЖдём прохождения анкет", "keyboard": key.get_keyboard(), "random_id": random.randint(2, 2147483647), 'dont_parse_links':1})

        ##Пройти анкету
            if body.lower()=='просто пройти анкеты':
                count_code=dict()
                dict_code=dict()
                count_code = try_file_reading("count_code.json") #файл с кодами отправленными пользователями
                count_code_keys=count_code.keys()
                if str(id) in count_code_keys:
                    dict_code=count_code[str(id)]
                count_code[str(id)+'P&D']='P'
                count_code[str(id)]=dict_code
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
                ind=[]
                indexx=[]
                for i in range(len(cou)):
                    indexx.append(i)
                dict_min1=dict(zip(indexx, cou))
                list_min=list(dict_min1.items())
                (list_min).sort(key=lambda i:i[1])
                dict_min=dict()
                for i in list_min:
                    dict_min[i[0]]=i[1]
                ind=list(dict_min.keys())[:5]
                anketa_str=''
                for i in ind:
                    anketa_str+=ssl[i]+'\n'

                anketa_str+='\nВот список актуальных анкет. \nКак пройдёте одну из них, пришлите, пожалуйста, код, который находиться в конце анкеты, он имеет вид: \nF-***'
                vk.method("messages.send", {"peer_id": id, "message": anketa_str + "\nЖдём прохождения анкет", "keyboard": key.get_keyboard(), "random_id": random.randint(2, 2147483647), 'dont_parse_links':1})
        ##База
            numb_code=[]
            count_code=dict()
            dict_code=dict()
            count_code = try_file_reading("count_code.json") #файл с кодами отправленными пользователями
            count_code_keys=count_code.keys()
            if str(id) in count_code_keys:
                dict_code=count_code[str(id)]
                for i in dict_code.keys():
                    if i != "finished" and i != "status" :
                        numb_code.append(dict_code[i])
            cod_lower=[]
            for i in cod:
                cod_lower.append(i.lower())
            list_dop=[]

            check=0

        ##Риски
            if body.lower()=='назад':
                count_code[str(id)+'P&D']='0'
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
                vk.method("messages.send", {"peer_id": id, "message":"Выберите что хотие сделать", "keyboard": key1.get_keyboard(), "random_id": random.randint(2, 2147483647)})

            if body.lower()=='в анкете нет кода':
                if count_code[str(id)+'P&D']=='D':
                    count_code[str(id)+'P&D']='D del'
                if count_code[str(id)+'P&D']=='P':
                    count_code[str(id)+'P&D']='P del'
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
                vk.method("messages.send", {"peer_id": id, "message":"Пришлите, пожалуйста, ссылку на эту анкету", "random_id": random.randint(2, 2147483647)})
            if body in ssl and (count_code[str(id)+'P&D']=='P del' or count_code[str(id)+'P&D']=='D del'):
                count_code['del']=body
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()
                vk.method("messages.send", {"peer_id": id, "message":f'У этой {body} анкеты нет кода, верно? \nЕсли да, по нажмите <<подтвердить>>', "keyboard": key2.get_keyboard(), "random_id": random.randint(2, 2147483647)})
            if body.lower()=='подтвердить':
                dell=count_code['del']
                if count_code[str(id)+'P&D']=='D del':
                    count_code[str(id)+'P&D']='D'
                if count_code[str(id)+'P&D']=='P del':
                    count_code[str(id)+'P&D']='P'
                count_code['del']=''
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()

                for i in permited_id:
                    vk.method("messages.send", {"peer_id": i, "message":f'У анкеты {dell} нет кода, её нужно удалить', "random_id": random.randint(2, 2147483647)})
                fid=333624601
                for u in j_new:
                    if u[1]==body:
                        fid=int(u[0])
                vk.method("messages.send", {"peer_id": fid, "message":f'У вашей анкеты {dell} нет кода', "random_id": random.randint(2, 2147483647)})
                dop_anketa_str='Спасибо, вот другая анкета: '
                ind=[]
                indexx=[]
                for i in range(len(cou)):
                    indexx.append(i)
                dict_min1=dict(zip(indexx, cou))
                list_min=list(dict_min1.items())
                (list_min).sort(key=lambda i:i[1])
                dict_min=dict()
                for i in list_min:
                    dict_min[i[0]]=i[1]
                ind=list(dict_min.keys())
                if count_code[str(id)+'P&D']=='D':
                    dop_anketa_str+=str(ssl[ind[3]])
                    vk.method("messages.send", {"peer_id": id, "message":dop_anketa_str, "random_id": random.randint(2, 2147483647)})
                    vk.method("messages.send", {"peer_id": id, "message":"Можете продолжить", "keyboard": key.get_keyboard(), "random_id": random.randint(2, 2147483647)})
                if count_code[str(id)+'P&D']=='P':
                    dop_anketa_str+=str(ssl[ind[6]])
                    vk.method("messages.send", {"peer_id": id, "message":dop_anketa_str, "random_id": random.randint(2, 2147483647)})
                    vk.method("messages.send", {"peer_id": id, "message":"Можете продолжить", "keyboard": key.get_keyboard(), "random_id": random.randint(2, 2147483647)})

            delit_list=[]
            if id in permited_id:
                if body.lower()[:8]=='!удалить':
                    delit_list1=body.lower().split()
                    vk.method("messages.send", {"peer_id": id, "message":delit_list1[1], "random_id": random.randint(2, 2147483647)})
                    for j in delit_list1:
                        if j in ssl:
                            delit_list.append(j)
                            vk.method("messages.send", {"peer_id": id, "message":delit_list[0], "random_id": random.randint(2, 2147483647)})


        ##Если добавить анкеты
            if count_code[str(id)+'P&D']=='D':
                ##Коды
                kckod=random.randint(100,999)
                kckod='F-'+str(kckod)
                while kckod in cod:
                    kckod=random.randint(100,999)
                    kckod='F-'+str(kckod)
                ckod='Вот ваш код:'+str(kckod)+'\nВставьте его, пожалуйста, в конец анкеты'
                T = 0

                if len(dict_code)<len(j_new):
                    if body.lower()[:7]!='анкета:':
                        if 'f-' in body.lower():
                            for i in range(len(body)):
                                f_='f-'
                                if body.lower()[i]=='f' and body.lower()[i+1]=='-':
                                    for j in body.lower()[i+2:i+5]:
                                        if j in '0123456789':
                                            check=1
                                        if i+5<len(body.lower()):

                                            if body.lower()[i+5] in '0123456789qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё:-/*+&^%$#@!~`?\|'  :
                                                check=0
                                        if body.lower()[i-1] in '0123456789qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё:-/*+&^%$#@!~`?\|' and i!=0 :

                                            check=0
                                    if check==1:
                                        f_+=body.lower()[i+2:i+5]
                                if len(f_)==5 and count_code[str(id)]["finished"] != True:
                                    if f_ in cod_lower:
                                        if f_ in numb_code:
                                            vk.method("messages.send", {"peer_id": id, "message": f'Вы уже ввели этот код {f_}', "random_id": random.randint(2, 2147483647)})
                                        else:
                                            numb_code.append(f_)
                                            list_dop.append(f_)
                                            if len(cod_lower)>=3:
                                                zzz=3
                                            else:
                                                zzz=len(cod_lower)
                                            ostat=zzz-len(numb_code)    #Количество уже заполненных пользователем анкет
                                            if ostat==2:
                                                answer='Спасибо, код '+(f_)+' принят, осталось ещё '+str(ostat)+' кода'
                                                vk.method("messages.send", {"peer_id": id, "message": answer, "random_id": random.randint(2, 2147483647)})
                                            if ostat==1:
                                                answer='Спасибо, код '+(f_)+' принят, остался ещё '+str(ostat)+' код'
                                                vk.method("messages.send", {"peer_id": id, "message": answer, "random_id": random.randint(2, 2147483647)})
                                            if ostat==0:
                                                vk.method("messages.send", {"peer_id": id, "message": f'Коды приняты. Спасибо за уделённое время\n{ckod}', "random_id": random.randint(2, 2147483647)})
                                                vk.method("messages.send", {"peer_id": id, "message": 'Пожалуйста, предоставьте всю необходимую информацию об анкете.\nПришлите ссылку на анкету', "random_id": random.randint(2, 2147483647)})

                                                #Маркеры для начала работы по дабвлению анкеты + часть данных об анкете
                                                count_code[str(id)]["finished"] = True
                                                count_code[str(id)]["status"] = 0
                                                count_code[str(id) + "_create"] = [id, kckod]
                                                glob_flag = 1

                                            if ostat<0:
                                                vk.method("messages.send", {"peer_id": id, "message": f'Спасибо, что решили пройти анкеты ещё, мы их зачтём', "random_id": random.randint(2, 2147483647)})
                                    else:
                                        vk.method("messages.send", {"peer_id": id, "message": f'Неверные код {f_} или формат записи, попробуйте ещё', "random_id": random.randint(2, 2147483647)})
                            if check!=1:
                                vk.method("messages.send", {"peer_id": id, "message": f'Неверные код или формат записи, попробуйте ещё', "random_id": random.randint(2, 2147483647)})


        ##Если просто пройти анкеты
            if count_code[str(id)+'P&D']=='P':
                if len(dict_code)<len(j_new):
                    if body.lower()[:7]!='анкета:':
                        if 'f-' in body.lower():
                            for i in range(len(body)):
                                f_='f-'
                                if body.lower()[i]=='f' and body.lower()[i+1]=='-':
                                    for j in body.lower()[i+2:i+5]:
                                        if j in '0123456789':
                                            check=1
                                        if i+5<len(body.lower()):

                                            if body.lower()[i+5] in '0123456789qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё:-/*+&^%$#@!~`?\|' :
                                                check=0
                                        if body.lower()[i-1] in '0123456789qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё:-/*+&^%$#@!~`?\|' and i!=0 :

                                            check=0
                                    if check==1:
                                        f_+=body.lower()[i+2:i+5]
                                if len(f_)==5:
                                    check_result = check_code(f_, id)
                                    vk.method("messages.send", {"peer_id": id, "message": "Код есть, ума не надо" + str(check_result) + f_, "random_id": random.randint(2, 2147483647)})

                                    if f_ in cod_lower:

                                        if f_ in numb_code or check_result == 1:
                                            vk.method("messages.send", {"peer_id": id, "message": f'Вы уже ввели этот код {f_}', "random_id": random.randint(2, 2147483647)})

                                        elif check_result == 0:
                                            numb_code.append(f_)
                                            list_dop.append(f_)
                                            vk.method("messages.send", {"peer_id": id, "message": f'Спасибо, код '+(f_)+' принят', "random_id": random.randint(2, 2147483647)})
                                    elif check_code(f_, id) == 1:
                                        vk.method("messages.send", {"peer_id": id, "message": f'Вы уже ввели этот код {f_}', "random_id": random.randint(2, 2147483647)})


        ##Счётчик прохождений на добавку
            if count_code[str(id)+'P&D']=='D':
                for i in range(len(numb_code)):
                    dict_code[str(i)]=numb_code[i]
                count_code[str(id)]=dict_code
                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                    write_file.close()

        ##Счётчик прохождения анкет бд
            for i in list_dop:
                for u in j_new:
                    if u[5].lower()==i:
                        u[4]+=1
                        if u[1] + ":" + str(id) not in fin_quests:   #######Этот человек ещё не заполнял эту анкету
                            fin_quests[u[1] + ":" + str(id)] = dt.date.today()
            #

        ##Удаление по команде

            count=0
            if delit_list!=[]:
                for i in delit_list:
                    spisok=[]
                    for u in j_new:
                        if (u[1])!=i:
                            spisok.append(u)
                        else:
                            count+=1
                    j_new=spisok
            if count>0:
                vk.method("messages.send", {"peer_id": id, "message": f'Анкета удалена', "random_id": random.randint(2, 2147483647)})


            ###### Запись в файл БД
            with open('prob.csv','w', encoding="utf-8") as w_file:
                    file_writer = csv.writer(w_file)
                    for i in j_new:
                        file_writer.writerow(i)
            w_file.close()
            ###### Запись в файл персональных отметок
            with open('filled_quests.json','w') as write_file:
                json.dump(fin_quests, write_file)
            write_file.close()


            numb_code=[]
            count_code=dict()
            dict_code=dict()
            count_code = try_file_reading("count_code.json") #файл с кодами отправленными пользователями
            count_code_keys=count_code.keys()
            if str(id) in count_code_keys:
                dict_code=count_code[str(id)]
                for i in dict_code.values():
                    numb_code.append(i)
    ###Добавление анкеты по шаблону########################################################################################################################################
            if count_code[str(id) + "P&D"] == "D" and count_code[str(id)]["finished"] == True and body.lower() != '' and glob_flag == 0:

                added_text = body.lower()
                status = int(count_code[str(id)]["status"])

                if status == 0: #Добавляем ссылку на анкету (обязательно в полной форме)
                    if check_url(added_text) == True:
                        for i in j_new:
                            if i[1] == added_text:
                                vk.method("messages.send", {"peer_id": id, "message": 'Анкета с такой ссылкой уже есть в базе.', "random_id": random.randint(2, 2147483647)})
                                return"ok"

                        count_code[str(id) + "_create"].append(added_text)
                        count_code[str(id)]["status"] = status + 1
                        vk.method("messages.send", {"peer_id": id, "message": 'Ссылка добавлена. Введите желаемое число заполнений', "random_id": random.randint(2, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": 'Неверный формат ссылки. Пожалуйста повторите попытку ввода', "random_id": random.randint(2, 2147483647)})

                elif status == 1: #Добавляем необходимое число прохождений
                    try:
                        added_text = int(added_text)
                        count_code[str(id) + "_create"].append(added_text)
                        count_code[str(id)]["status"] = status + 1
                        vk.method("messages.send", {"peer_id": id, "message": 'Значение добавлено. Введите крайний срок заполнения анкеты в формате гггг-мм-дд', "random_id": random.randint(2, 2147483647)})
                    except ValueError:
                        vk.method("messages.send", {"peer_id": id, "message": 'Чтобы указать, сколько Вам нужно ответов, введите число', "random_id": random.randint(2, 2147483647)})

                elif status == 2:
                    #Проверка правильного формата даты
                    try:
                        test_test_test = dt.datetime.strptime(added_text, '%Y-%m-%d').date()
                    except:
                        vk.method("messages.send", {"peer_id": id, "message": f'Неверный формат даты. Пожалуйста повторите попытку ввода', "random_id": random.randint(2, 2147483647)})
                        return "ok"

                    count_code[str(id) + "_create"].append(added_text)
                    count_code[str(id)]["status"] = status + 1
                    vk.method("messages.send", {"peer_id": id, "message": 'Крайний срок сохранён. Введите текущее количество заполнивших (или 0, если таких нет)', "random_id": random.randint(2, 2147483647)})

                elif status == 3: #Добавляем текущее количество прохождений
                    try:
                        added_text = int(added_text)
                        count_code[str(id) + "_create"].append(added_text)
                        count_code[str(id)]["status"] = status + 1
                    except ValueError:
                        vk.method("messages.send", {"peer_id": id, "message": 'Чтобы указать, сколько сейчас ответов на анкету, введите число', "random_id": random.randint(2, 2147483647)})
                        return "ok"

                    #Создаём новую строку записи в БД
                    stal1 = count_code[str(id) + "_create"]
                    stal = [i for i in range(5)]
                    stal = [stal1[0], stal1[2], stal1[3], dt.datetime.strptime(stal1[4], '%Y-%m-%d').date(), stal1[5], stal1[1].lower()]

                    j_new.append(stal)

                    #Откатываем маркеры работы до состояния - начало работы
                    del count_code[str(id) + "_create"]
                    count_code[str(id)+'P&D']='0'
                    count_code[str(id)]=dict()

                    chel=str(stal[1])+':'+str(id)
                    fin_quests[chel]=dt.date.today()

                    vk.method("messages.send", {"peer_id": id, "message": f'Спасибо.\nПожалуйста не забудьте добавить код({stal1[1]}) на отдельный лист в конец анкеты, иначе другие пользователи не смогут её пройти', "random_id": random.randint(2, 2147483647)})
                    vk.method("messages.send", {"peer_id": id, "message":"выберите что хотие сделать", "keyboard": key1.get_keyboard(), "random_id": random.randint(2, 2147483647)})



                ###### Дозапись в файл БД
                with open('prob.csv','w', encoding="utf-8") as w_file:
                        file_writer = csv.writer(w_file)
                        for i in j_new:
                            file_writer.writerow(i)
                w_file.close()
                ###### Дозапись в файл персональных отметок
                with open('filled_quests.json','w') as write_file:
                    json.dump(fin_quests, write_file)
                write_file.close()

                with open('count_code.json','w') as write_file:
                    json.dump(count_code, write_file)
                write_file.close()

               #############конец работы
    except :
        # Сообщение админу об ошибке
        vk.method("messages.send", {"peer_id" : DEV_ID_SLAVA, "message" : (traceback.format_exc()+'\n\n'+str(data))[:4096], "random_id" : random.randint(1, 2147483647)})
        #vk.method("messages.send", {"peer_id" : DEV_ID_IANA, "message" : (traceback.format_exc()+'\n\n'+str(data))[:4096], "random_id" : random.randint(1, 2147483647)})
    return "ok"








