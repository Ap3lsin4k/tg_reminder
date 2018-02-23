# -*- coding: utf-8 -*-
import telebot
from telebot import types
import datetime
# from time_calendar import create_calendar, create_watch
import constans
import myClass
import g  # global

#bot = myClass.bot # idea
bot = telebot.TeleBot(constans.token)


def log(message):
    print("======", datetime.datetime.now())
    print("message:", message.text)
    print("g.location", g.location)
    print("GROUP:", g.group)
    for note_name in myClass.work.some_group:
        print("\'{}\': ".format(note_name), myClass.work.some_group[note_name])
    print()
    pass
    # print("\n------ begin")
    # print(datetime.datetime.now())
    # print("Lang:", g.lang)
    # print("Location:", g.location)
    # print("Group:", g.group)
    # print("Work:", myClass.work.some_group)
    # print("(current_shown_dates):", myClass.work.current_shown_dates)
    # print(myClass.work.time)
    # print("count edit note work:", str(myClass.work.edit_note_work))
    # print("\n------ end")


def main_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    if g.lang == 'ru':
        user_markup.row('Рабочие', 'Домашние')  # 💼🏢 🏠
        user_markup.row('Срочные')  # ⏰
        user_markup.row('Настройки', 'Другие')  # ⚙ \u****
        user_markup.row('Добавить группу', 'Назад')  # + \u**** 🔙
        bot.send_message(message.from_user.id, 'Вы в главном меню.', reply_markup=user_markup)
    else:
        user_markup.row('Workers', 'Home')  # 🏠
        user_markup.row('Urgent')
        user_markup.row('Settings', 'Other')
        user_markup.row('Add group', 'Back')
        bot.send_message(message.from_user.id, 'You are in the main menu.', reply_markup=user_markup)
        'You are in the main menu'


def workers(message):
    myClass.work.main(bot, message, g.lang)


def home(message):
    myClass.home.main(bot, message, g.lang)


def urgent(message):
    myClass.urgent.main(bot, message, g.lang)



def other(message):
    print("hello from def other(message):")
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    for i in range(0, len(g.group), 2):
        if (i + 1) < len(g.group):
            user_markup.row(g.group[i], g.group[i + 1])  # Виводим красиво по 2 кнопки на ряд
        else:
            user_markup.row(g.group[i])

    if g.lang == 'ru':
        user_markup.row("Назад")  # 'Добавить группу'
        bot.send_message(message.from_user.id, "Вы в меню \"Другие\"", reply_markup=user_markup)
    else:
        user_markup.row("Back")
        bot.send_message(message.from_user.id, "You are in the menu \"Others\"", reply_markup=user_markup)
    # else:
    #     for i in range(len(group)):
    #         user_markup.add(group[i])
    #     user_markup.row('Back')
    #     bot.send_message(message.from_user.id, , reply_markup=user_markup)


def some_other_group(message):
    myClass.other[g.count_name_group_other].main(bot, message, g.lang)


def sett_lang(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Русский', 'English')

    if g.lang == 'ru':
        user_markup.row('Назад')
        bot.send_message(message.from_user.id, "Вы в настройках.", reply_markup=user_markup)
    else:
        user_markup.row('Back')
        bot.send_message(message.from_user.id, "You are in the settings.", reply_markup=user_markup)



def add_group(message):
    g.group.append(message.text)
    myClass.other[message.text] = myClass.NOTE(message.text)

    if g.lang == 'ru':
        bot.send_message(message.from_user.id,
                         'Вы создали новую группу под названием: {}'.format(message.text))  # group[-1]
    else:
        bot.send_message(message.from_user.id, 'You created a new group called: {}'.format(message.text))

    g.location = ['main_menu']
    main_menu(message)


# Привітання
@bot.message_handler(commands=['start'])
def handle_start(message):
    g.location = ['main_menu']
    g.group = []
    if g.lang == 'ru':
        bot.send_message(message.from_user.id, "Добро пожаловать!")
    else:
        bot.send_message(message.from_user.id, "Welcome!")
    main_menu(message)  # згенерировать клавиатуру меню


# Стоп
@bot.message_handler(commands=['stop'])
def hendle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    if g.lang == 'ru':
        bot.send_message(message.from_user.id, 'Пока!', reply_markup=hide_markup)
    else:
        bot.send_message(message.from_user.id, 'Goodbye!', reply_markup=hide_markup)


# изминения языка
@bot.message_handler(content_types=['text'])
def handle_language(message):
    if g.location == ['main_menu']:
        if message.text == 'Рабочие' or message.text == 'Workers':
            g.location = ['workers']
            workers(message)
        elif message.text == 'Домашние' or message.text == 'Home':
            g.location = ['home']
            home(message)
        elif message.text == 'Срочные' or message.text == 'Urgent':
            g.location = ['urgent']
            urgent(message)
        elif message.text == 'Настройки' or message.text == 'Settings':
            g.location = ['settings']
            sett_lang(message)
        elif message.text == 'Другие' or message.text == 'Other':
            g.location = ['other']
            other(message)
        elif message.text == 'Добавить группу' or message.text == 'Add group':
            g.location = ['add_group']
            hide_markup = telebot.types.ReplyKeyboardRemove()
            if g.lang == 'ru':
                bot.send_message(message.from_user.id, "Введите название группы:", reply_markup=hide_markup)
            else:
                bot.send_message(message.from_user.id, "Enter group name:", reply_markup=hide_markup)

    elif g.location[0] == 'workers':
        if g.location == ['workers']:
            if message.text == 'Добавить заметку' or message.text == 'Add note':
                g.location.append('add_note')
                myClass.work.add_note(bot, message, g.lang)
            elif message.text == 'Назад' or message.text == 'Back':
                g.location = ['main_menu']
                main_menu(message)
        elif g.location[1] == 'add_note':
            g.location[1] = 'add_note_time1'
            myClass.work.add_note_name(message.text)
            myClass.work.get_calendar(bot, message, g.lang)# викликаємо генерацію календаря
            # коли натиснемо на календар, зміниться  g.location[1]  'add_note_time1' -> 'add_note_time2'
        elif g.location[1] == 'add_note_time2':  # коли вибрали час
            if message.text == "Дальше" or message.text == "OK":
                g.location[1] = 'add_note_description'
                myClass.work.add_note_time(bot, message, g.lang)
        elif g.location[1] == 'add_note_description':
            g.location = ['workers']
            myClass.work.add_note_description(message)
            #print("myClass.work.some_group:", myClass.work.some_group)
            workers(message)

    elif g.location[0] == 'home':
        if g.location == ['home']:
            if message.text == 'Добавить заметку' or message.text == 'Add note':
                g.location.append('add_note')
                myClass.home.add_note(bot, message, g.lang)
            elif message.text == 'Назад' or message.text == 'Back':
                g.location = ['main_menu']
                main_menu(message)
        elif g.location[1] == 'add_note':
            g.location[1] = 'add_note_time1'
            myClass.home.add_note_name(message.text)
            myClass.home.get_calendar(bot, message, g.lang)  # викликаємо генерацію календаря
            # коли натиснемо на календар, зміниться  g.location[1]  'add_note_time1' -> 'add_note_time2'
        elif g.location[1] == 'add_note_time2':  # коли вибрали час
            if message.text == "Дальше" or message.text == "OK":
                g.location[1] = 'add_note_description'
                myClass.home.add_note_time(bot, message, g.lang)
        elif g.location[1] == 'add_note_description':
            g.location = ['home']
            myClass.home.add_note_description(message)
            # print("myClass.work.some_group:", myClass.work.some_group)
            home(message)

    elif g.location[0] == 'urgent':
        if g.location == ['urgent']:
            if message.text == 'Добавить заметку' or message.text == 'Add note':
                g.location.append('add_note')
                myClass.urgent.add_note(bot, message, g.lang)
            elif message.text == 'Назад' or message.text == 'Back':
                g.location = ['main_menu']
                main_menu(message)
        elif g.location[1] == 'add_note':
            g.location[1] = 'add_note_time1'
            myClass.urgent.add_note_name(message.text)
            myClass.urgent.get_calendar(bot, message, g.lang)  # викликаємо генерацію календаря
            # коли натиснемо на календар, зміниться  g.location[1]  'add_note_time1' -> 'add_note_time2'
        elif g.location[1] == 'add_note_time2':  # коли вибрали час
            if message.text == "Дальше" or message.text == "OK":
                g.location[1] = 'add_note_description'
                myClass.urgent.add_note_time(bot, message, g.lang)
        elif g.location[1] == 'add_note_description':
            g.location = ['home']
            myClass.urgent.add_note_description(message)
            # print("myClass.work.some_group:", myClass.work.some_group)
            urgent(message)
        # if message.text == 'Назад' or message.text == 'Back':
        #     g.location = ['main_menu']
        #     main_menu(message)

    elif g.location[0] == 'other':
        if message.text == 'Назад' or message.text == 'Back':
             g.location = ['main_menu']
             main_menu(message)
        elif g.location == ['other']:
            for name_group_other in g.group:
                if name_group_other == message.text:
                    bot.send_message(message.from_user.id, "Вы нажали на групу " + name_group_other)
                    g.location.append(name_group_other)
                    g.count_name_group_other = name_group_other
                    myClass.other[g.count_name_group_other].main(bot, message, g.lang)
                    break
                # name_group_outher група на которую нажали
        elif g.location == ['other', g.count_name_group_other]:
            if message.text == 'Добавить заметку' or message.text == 'Add note':
                g.location.append('add_note')
                myClass.other[g.count_name_group_other].add_note(bot, message, g.lang)
            elif message.text == 'Назад' or message.text == 'Back':
                g.location = ['main_menu']
                main_menu(message)
        elif g.location[2] == 'add_note':
            g.location[2] = 'add_note_time1'
            myClass.other[g.count_name_group_other].add_note_name(message.text)
            myClass.other[g.count_name_group_other].get_calendar(bot, message, g.lang)  # викликаємо генерацію календаря
            # коли натиснемо на календар, зміниться  g.location[2]  'add_note_time1' -> 'add_note_time2'
        elif g.location[2] == 'add_note_time2':  # коли вибрали час
            if message.text == "Дальше" or message.text == "OK":
                g.location[2] = 'add_note_description'
                myClass.other[g.count_name_group_other].add_note_time(bot, message, g.lang)
        elif g.location[2] == 'add_note_description':
            g.location = ['other', g.count_name_group_other]  # debug
            myClass.other[g.count_name_group_other].add_note_description(message)
            # print("myClass.work.some_group:", myClass.work.some_group)
            some_other_group(message)


    elif g.location == ['settings']:
        if message.text == "English":
            g.lang = 'en'
            sett_lang(message)
        elif message.text == "Русский":
            g.lang = 'ru'
            sett_lang(message)
        elif message.text == 'Назад' or message.text == 'Back':
            g.location = ['main_menu']
            main_menu(message)

    elif g.location == ['add_group']:
        add_group(message)
    log(message)


# calendar handle
# inline create
# @bot.message_handler(commands=['calendar'])


# inline handle
@bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
def get_day(call):
    # якщо функція нормально спрацювала повертається 'workers/add_note_time2',
    if g.location[0] == 'workers':
        g.location = myClass.work.get_day(bot, call, g.location, g.lang, 1)  # інакше повертається місце де ми зараз є ('workers/add_note_time1')
    elif g.location[0] == 'home':
        g.location = myClass.home.get_day(bot, call, g.location, g.lang, 1)
    elif g.location[0] == 'urgent':
        g.location = myClass.urgent.get_day(bot, call, g.location, g.lang, 1)
    elif g.location[0] == 'other':
        g.location = myClass.other[g.count_name_group_other].get_day(bot, call, g.location, g.lang, 2)


@bot.callback_query_handler(func=lambda call: call.data == 'next-month')
def next_month(call):
    if g.location[0] == 'workers':
        myClass.work.next_month(bot, call, g.lang)
    elif g.location[0] == 'home':
        myClass.home.next_month(bot, call, g.lang)
    elif g.location[0] == 'urgent':
        myClass.urgent.next_month(bot, call, g.lang)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].next_month(bot, call, g.lang)


@bot.callback_query_handler(func=lambda call: call.data == 'previous-month')
def previous_month(call):
    if g.location[0] == 'workers':
        myClass.work.previous_month(bot, call, g.lang)
    elif g.location[0] == 'home':
        myClass.home.previous_month(bot, call, g.lang)
    elif g.location[0] == 'urgent':
        myClass.urgent.previous_month(bot, call, g.lang)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].previous_month(bot, call, g.lang)


@bot.callback_query_handler(func=lambda call: call.data == 'hours' or call.data == 'hours_inc')
def hours_increment(call):
    if g.location[0] == 'workers':
        myClass.work.hours_increment(bot, call)
    elif g.location[0] == 'home':
        myClass.home.hours_increment(bot, call)
    elif g.location[0] == 'urgent':
        myClass.urgent.hours_increment(bot, call)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].hours_increment(bot, call)


@bot.callback_query_handler(func=lambda call: call.data == 'hours_dec')
def hours_decrement(call):
    if g.location[0] == 'workers':
        myClass.work.hours_decrement(bot, call)
    elif g.location[0] == 'home':
        myClass.home.hours_decrement(bot, call)
    elif g.location[0] == 'urgent':
        myClass.urgent.hours_decrement(bot, call)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].hours_decrement(bot, call)


@bot.callback_query_handler(func=lambda call: call.data == 'minut_inc')
def minut_increment(call):
    if g.location[0] == 'workers':
        myClass.work.minut_increment(bot, call)
    elif g.location[0] == 'home':
        myClass.home.minut_increment(bot, call)
    elif g.location[0] == 'urgent':
        myClass.urgent.minut_increment(bot, call)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].minut_increment(bot, call)


@bot.callback_query_handler(func=lambda call: call.data == 'minutes')
def minutes_increment(call):
    if g.location[0] == 'workers':
        myClass.work.minutes_increment(bot, call)
    elif g.location[0] == 'home':
        myClass.home.minutes_increment(bot, call)
    elif g.location[0] == 'urgent':
        myClass.urgent.minutes_increment(bot, call)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].minutes_increment(bot, call)


@bot.callback_query_handler(func=lambda call: call.data == 'minut_dec')
def minut_decrement(call):
    if g.location[0] == 'workers':
        myClass.work.minut_decrement(bot, call)
    elif g.location[0] == 'home':
        myClass.home.minut_decrement(bot, call)
    elif g.location[0] == 'urgent':
        myClass.urgent.minut_decrement(bot, call)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].minut_decrement(bot, call)


@bot.callback_query_handler(func=lambda call: call.data == 'ignore')
def ignore(call):
    if g.location[0] == 'workers':
        myClass.work.ignore(bot, call)
    elif g.location[0] == 'home':
        myClass.home.ignore(bot, call)
    elif g.location[0] == 'urgent':
        myClass.urgent.ignore(bot, call)
    elif g.location[0] == 'other':
        myClass.other[g.count_name_group_other].ignore(bot, call)


bot.polling(none_stop=True, interval=0)


# TODO реалізувати додавання заміток до другие
# TODO коли добавляєш групу myClass.other['name_group'] = NOTE('name_group')
# TODO видалити g.group
# В другие добавить кнопку создать группу
# В группе додати кнопку создати замітку
# Додати emoji
# Перевірити global у всіх функціях
# Перевірити мову у всіх функціях
# Очистку данных при комманде stop
# Отменна при создании заметки
# Замінити chat на from_user
# Функцію скидання налаштувань
# Дата создания заметки
# При закінченні введення опису замітки виводити замітку і питати чи дійсно ви хочете її додати
# При введенні замітки реалізувати можливість пропустити
# виводити не 0 а 00
# Якщо до дати спрацювання замітки залишилось пару днів то виводити дату спрацювання замітки
# Якщо до дати спрацювання замітки в цей день то виводити годину:хвилину спрацювання
# Перевірити на баги якщо викликається workers а дата не введена
# подумати чи потрібно при натискані на кнопки ховати клавіатуру
# Вы создали новую заметку под названием
# Коментарії до g.py
# Переписати код під python2 щоб виставити його на хероку
# перевірити lang у всіх функціях
# years month days hours minutes -> time = {'years': "...", 'month': "...",  ...}
# При виборі дати міняти кнопки на кнопки годанника
# Видалити current_shown_dates
# додати Traceback для get_day(), next_month(), ...
# поміняти місцями опис до замітки і дату введення
# вводити дату по натисканні на кнопку Додати дату
# вводити час тільки при натисканні на кнопку додати час
# Виправити баг: коли після того як вводиш час нажати, не ОК а відправити якийсь текст кнопка пропадає
# Подумати як зменшити повторяючийся код в останніх 9 функціях
# для заметок в кортежі години і хвилини зберігати в str
# Опис до заміток при натисканні на замітку
# в меню налаштувань змінити часовий пояс
# додати появлення в срочних заміток