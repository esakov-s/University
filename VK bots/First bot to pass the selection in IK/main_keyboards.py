from flask import Flask, request, json
import vk_api
#Клавиатуры для этого бота (попробовать вынести в отдельный файл)

#Основная клавиатура
main_keyboard_menu = vk_api.VkKeyboard(one_time=False)
main_keyboard_menu.add_button("Контакты", "primary", {"type" : "contacts"})
main_keyboard_menu.add_button("Общежития", "primary", {"type" : "dorm"})
main_keyboard_menu.add_line()
main_keyboard_menu.add_button("Транспорт", "secondary", {"type" : "transport"})
main_keyboard_menu.add_line()
main_keyboard_menu.add_button("Записаться на вебинар", "primary", {"type" : "web"})
main_keyboard_menu.add_line()
main_keyboard_menu.add_button("Поднять настроение", "positive", {"type" : "smile"})
main_keyboard_menu.add_line()
main_keyboard_menu.add_button("Закончить работу", "negative", {"type" : "work_end"})


#Клавиатура общежитий
dorm_keyboard_menu = vk_api.VkKeyboard(one_time=False)
dorm_keyboard_menu.add_button("ул. Б. Галушкина", "primary", {"type" : "dorm", "dorm" : "b_gal"})
dorm_keyboard_menu.add_button("ул. Керченская", "primary", {"type" : "dorm", "dorm" : "kerch"})
dorm_keyboard_menu.add_line()
dorm_keyboard_menu.add_button("Лениградский проспект 51", "primary", {"type" : "dorm", "dorm" : "len_51"})
dorm_keyboard_menu.add_button("Лениградский проспект 55", "primary", {"type" : "dorm", "dorm" : "len_55"})
dorm_keyboard_menu.add_line()
dorm_keyboard_menu.add_button("ул. Новопесчаная", "primary", {"type" : "dorm", "dorm" : "nov_pes"})
dorm_keyboard_menu.add_button("ул. Балтийская", "primary", {"type" : "dorm", "dorm" : "balt"})
dorm_keyboard_menu.add_line()
dorm_keyboard_menu.add_button("Коломенский проезд", "primary", {"type" : "dorm", "dorm" : "kolom"})
dorm_keyboard_menu.add_line()
dorm_keyboard_menu.add_button("Стоимость общежитий", "secondary", {"type" : "dorm", "dorm" : "cost"})
dorm_keyboard_menu.add_line()
dorm_keyboard_menu.add_button("Вернуться", "negative", {"type" : "dorm", "dorm" : "back"})



#Клавиатура для возврата к первоначальному меню
reset_keyboard_menu = vk_api.VkKeyboard(one_time=False)
reset_keyboard_menu.add_button("Вернуться", "negative", {"type" : "return"})