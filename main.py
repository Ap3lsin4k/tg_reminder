# -*- coding: utf-8 -*-
import telebot
from telebot import types
import datetime
from time_calendar import create_calendar, create_watch
import constans
#

bot = telebot.TeleBot(constans.token)
# поточна мова, місце, нові групи, нові замітки у воркс
global lang, location
global group, work, edit_note_work
global years, month, days, hours, minutes# sec = 0 за замовчуванням
now = datetime.datetime.now()
years, month, days = now.year, now.month, now.day
hours, minutes = 12, 0
current_shown_dates = {}
lang = "en"
location = "main_menu"#{'main_menu': {'workers': 'workers/add_note'}, 'home', 'urgent', 'settings', 'other', 'add_group'}
group = []#{}
work = {}
edit_note_work = ""


def log(message):
    global lang, location, group, work, edit_note_work
    global hours, minutes, days, month, years
    print("\n------ begin")
    from datetime import datetime
    print(datetime.now())
    print("Lang:", lang)
    print("Location:", location)
    print("Group:", group)
    print("Work:", work)
    print("(current_shown_dates):", current_shown_dates)
    print(years, month, days, hours, minutes)
    print("count edit note work:", str(edit_note_work))

    # with open('log.txt', 'w') as f:
    #     f.write("\n------")
    #     from datetime import datetime
    #     f.write(datetime.now())
    #     f.write("Lang:", lang)
    #     f.write("Location:", location)
    #     f.write("Group:", group)
    print("\n------ end")

def main_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    if lang == 'ru':
        user_markup.row('Рабочие', 'Домашние')# 💼🏢 🏠
        user_markup.row('Срочные')# ⏰
        user_markup.row('Настройки', 'Другие')# ⚙ \u****
        user_markup.row('Добавить группу', 'Назад')# + \u**** 🔙
        bot.send_message(message.from_user.id, 'Вы в главном меню.', reply_markup=user_markup)
    else:
        user_markup.row('Workers', 'Home')# 🏠
        user_markup.row('Urgent')
        user_markup.row('Settings', 'Other')
        user_markup.row('Add group', 'Back')
        bot.send_message(message.from_user.id, 'You are in the main menu.', reply_markup=user_markup)
        'You are in the main menu'

def workers(message):
    global lang
    global location
    global group
    global work # ключ "" не виводити НІКОЛИ
    #work = {
    #    'go to eat': {'time': "10:00", 'description': "you go to eat, and start eat"},
        #'watch film': {'time': "12:00", 'descript': "this descript for watch film"},
        #'sleep': {'time': "21:00", 'descript': "go to bed and sleep"},
        # 'wake up': {'time': "9:00", 'descript': "WAAAKEEEEEE UUUUUUUUUUUP"}
    #};

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    for i in work:
        if i != "":  # для Debug
            #                                                                                                 день                           месяц                            год
            format_date = str(work[i]['time'][3]) + ":" + str(work[i]['time'][4]) + "\n" + str(work[i]['time'][2]) + "." + str(work[i]['time'][1]) + "." + str(work[i]['time'][0])
            user_markup.row(i, format_date)  # Вивести замітку і гарно відформатований час       18:36
            del format_date                  #                                                 21.2.2018
    if lang == 'ru':
        user_markup.row('Добавить заметку', 'Назад')
        bot.send_message(message.from_user.id, "Нажмите на заметку, чтобы её отредактировать", reply_markup=user_markup)
    else:
        user_markup.row('Add note', 'Back')
        bot.send_message(message.from_user.id, "Click on a note to edit it", reply_markup=user_markup)
def home(message):
    global lang
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    if lang == 'ru':
        user_markup.row('Добавить заметку', 'Назад')
        bot.send_message(message.from_user.id, "Нажмите на заметку, чтобы её отредактировать", reply_markup=user_markup)
    else:
        user_markup.row('Add note', 'Back')
        bot.send_message(message.from_user.id, "Click on a note to edit it", reply_markup=user_markup)
def urgent(message):
    global lang
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    if lang == 'ru':
        user_markup.row('Добавить заметку', 'Назад')
        bot.send_message(message.from_user.id, "Нажмите на заметку, чтобы её отредактировать", reply_markup=user_markup)
    else:
        user_markup.row('Add note', 'Back')
        bot.send_message(message.from_user.id, "Click on a note to edit it", reply_markup=user_markup)
def sett_lang(message):
    global lang
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Русский', 'English')
    user_markup.row('Назад' if lang == 'ru' else 'Back')
    if lang == 'ru':
        bot.send_message(message.from_user.id, "Вы в настройках.", reply_markup=user_markup)
    else:
        bot.send_message(message.from_user.id, "You are in the settings.", reply_markup=user_markup)
def other(message):
    global lang
    global location
    global group
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    for i in range(0, len(group), 2):
        if (i+1) < len(group):
            user_markup.row(group[i], group[i+1])
        else:
            user_markup.row(group[i])


    if lang == 'ru':
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
def add_group(message):
    global lang
    global location
    global group
    group.append(message.text)
    if lang == 'ru':
        bot.send_message(message.from_user.id, 'Вы создали новую группу под названием: {0}'.format(message.text))#group[-1]
    else:
        bot.send_message(message.from_user.id, 'You created a new group called: {0}'.format(message.text))
    location = 'main_menu'#debug
    main_menu(message)

#Привітання
@bot.message_handler(commands=['start'])
def handle_start(message):
    #init
    global lang, location
    # lang = 'en'#щоб при старті залишалась мова
    location = 'main_menu'
    global years, month, days, hours, minutes
    now = datetime.datetime.now()
    years, month, days = now.year, now.month, now.day
    hours, minutes = 12, 0
    current_shown_dates = {}
    group = []  # {}
    work = {}
    #
    if lang == 'ru':
        bot.send_message(message.from_user.id, "Добро пожаловать!")
    else:
        bot.send_message(message.from_user.id, "Welcome!")
    main_menu(message)#згенерировать клавиатуру меню


#Стоп
@bot.message_handler(commands=['stop'])
def hendle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    if lang == 'ru':
        bot.send_message(message.from_user.id, 'Пока!', reply_markup=hide_markup)
    else:
        bot.send_message(message.from_user.id, 'Goodbye!', reply_markup=hide_markup)

#изминения языка
@bot.message_handler(content_types=['text'])
def handle_language(message):
    global lang
    global location
    global group
    global work
    global edit_note_work  # (назва замітки) яка вказує, на словник параметрів замітки ('time': '...', 'descript':'...')

    if location == 'main_menu':
        if message.text == 'Рабочие' or message.text == 'Workers':
            location = 'workers'
            workers(message)
        elif message.text == 'Домашние' or message.text == 'Home':
            location = 'home'
            home(message)
        elif message.text == 'Срочные' or message.text == 'Urgent':
            location = 'urgent'
            urgent(message)
        elif message.text == 'Настройки' or message.text == 'Settings':
            location = 'settings'
            sett_lang(message)
        elif message.text == 'Другие' or message.text == 'Other':
            location = 'other'
            other(message)
        elif message.text == 'Добавить группу' or message.text == 'Add group':
            location = 'add_group'
            hide_markup = telebot.types.ReplyKeyboardRemove()
            if lang == 'ru':
                bot.send_message(message.from_user.id, "Введите название группы:", reply_markup=hide_markup)
            else:
                bot.send_message(message.from_user.id, "Enter group name:", reply_markup=hide_markup)

    elif location[:7] == 'workers':
        if location == 'workers/add_note':
            edit_note_work = message.text
            work[edit_note_work] = {}  # назва замітки є силкою на словник параметрів сторінки
            location = 'workers/add_note_time1' # вибір дня
            # if lang == 'ru':
            #     bot.send_message(message.from_user.id, 'Введите время:')
            # else:
            #     bot.send_message(message.from_user.id, 'Enter time:')
            get_calendar(message)  # викликаємо генерацію календаря
        elif location == 'workers/add_note_time2':  # вибір години
            if message.text == "Дальше" or message.text == "OK":
                work[edit_note_work]['time'] = (years, month, days, hours, minutes)
                location = 'workers/add_note_description'
                if lang == 'ru':
                    bot.send_message(message.from_user.id, "Введите описание заметки")
                else:
                    bot.send_message(message.from_user.id, "Enter a note description")
        elif location == 'workers/add_note_description':
            work[edit_note_work]['description'] = message.text
            edit_note_work = "" # для Debug
            print("work:", work)
            location = 'workers'
            workers(message)

        #location == workers
        elif location == 'workers':
            if message.text == 'Добавить заметку' or message.text == 'Add note':
                location += '/'+'add_note'
                hide_markup = telebot.types.ReplyKeyboardRemove()
                if lang == 'ru':
                    bot.send_message(message.from_user.id, "Введите название заметки", reply_markup=hide_markup)
                else:
                    bot.send_message(message.from_user.id, "Enter a note name", reply_markup=hide_markup)
                    #continue work

            elif message.text == 'Назад' or message.text == 'Back':
                location = 'main_menu'
                main_menu(message)
    elif location == 'home':
        if message.text == 'Назад' or message.text == 'Back':
            location = 'main_menu'
            main_menu(message)
    elif location == 'urgent':
        if message.text == 'Назад' or message.text == 'Back':
            location = 'main_menu'
            main_menu(message)
    elif location == 'settings':
        if message.text == "English":
            lang = 'en'
            sett_lang(message)
        elif message.text == "Русский":
            lang = 'ru'
            sett_lang(message)
        elif message.text == 'Назад' or message.text == 'Back':
            location = 'main_menu'
            main_menu(message)
    elif location == 'other':
        #add group
        # if message.text in group:
        #     location += '/'+message.text
        #     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        #     if lang == 'ru':
        #         user_markup.row('Добавить заметку')
        #     else:
        #         user_markup.row('Add note')
        if message.text == 'Назад' or message.text == 'Back':
            location = 'main_menu'
            main_menu(message)

    elif location == 'add_group':
        add_group(message)
        #debug test
    log(message)

#calendar handle
    #inline create
@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    global lang
    global hours, minutes
    hours, minutes = 12, 0#Стандартні параметри
    now = datetime.datetime.now()  # Current date
    date = (now.year, now.month)
    current_shown_dates[message.from_user.id] = date  # Saving the current date in a dict
    markup = create_calendar(now.year, now.month) # створюємо inline calendar
    if lang == 'ru':
        bot.send_message(message.chat.id, "Выберите дату", reply_markup=markup)  # виводимо календар
    else:
        bot.send_message(message.chat.id, "Please, choose a date", reply_markup=markup)# виводимо календар
    # get_watch(message)

@bot.message_handler(commands=['clock'])#delete func
def get_watch(message):
     global hours, minutes
     markup = create_watch(hours, minutes)
     bot.send_message(message.chat.id, "Chose hourse", reply_markup=markup)

    #inline handle
@bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
def get_day(call):
    global work
    global edit_note_work
    global location, lang
    global years, month, days, hours, minutes
    print(call.data, call)
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if (saved_date is not None):
        print("saved_date: ", saved_date)
        day = call.data[13:] #день на который нажал юзер
        date = datetime.datetime(int(saved_date[0]), int(saved_date[1]), int(day), hours, minutes)
        years = int(saved_date[0])
        month = int(saved_date[1])
        days = int(day)
        bot.send_message(chat_id, str(date))
        bot.answer_callback_query(call.id, text="")

        if location == 'workers/add_note_time1':
            location = 'workers/add_note_time2'
            # get_watch()
            if lang == 'ru':
                bot.send_message(call.from_user.id, "Выберете время", reply_markup=create_watch(hours, minutes))
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row("Дальше")
                bot.send_message(call.from_user.id, "И нажмите на кнопку \"Дальше\"",
                                 reply_markup=user_markup)
            else:
                bot.send_message(call.from_user.id, "Select the time", reply_markup=create_watch(hours, minutes))
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row("OK")
                bot.send_message(call.from_user.id, "And click on the button \"OK\"",
                                 reply_markup=user_markup)

    else:
        # Do something to inform of the error
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'next-month')
def next_month(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if saved_date is not None:
        year, month = saved_date
        month += 1
        if month > 12:
            month = 1
            year += 1
        date = (year, month)
        current_shown_dates[chat_id] = date
        markup = create_calendar(year, month)
        bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        # Do something to inform of the error
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'previous-month')
def previous_month(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if saved_date is not None:
        year, month = saved_date
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        date = (year, month)
        current_shown_dates[chat_id] = date
        markup = create_calendar(year, month)
        bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        # Do something to inform of the error
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'hours' or call.data == 'hours_inc')
def hours_increment(call):
    global hours, minutes
    hours += 1
    if hours >= 24:
        hours -= 24
    print("hours and minutes:", hours, minutes)
    bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                  message_id=call.message.message_id,
                                  reply_markup=create_watch(hours, minutes)
                                  )
    # bot.edit_message_text(chat_id=call.from_user.id,
    #                       message_id=call.message.message_id,
    #                       text="lol",
    #                       )


@bot.callback_query_handler(func=lambda call: call.data == 'hours_dec')
def hours_decrement(call):
    global hours, minutes
    hours -= 1
    if hours < 0:
        hours += 24
    print("hours and minutes:", hours, minutes)
    bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                  message_id=call.message.message_id,
                                  reply_markup=create_watch(hours, minutes))

@bot.callback_query_handler(func=lambda call: call.data == 'minut_inc')
def minut_increment(call):
    global hours, minutes
    minutes += 10
    if minutes >= 60:
        minutes -= 60  # обнуление счетчика
    bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                  message_id=call.message.message_id,
                                  reply_markup=create_watch(hours, minutes))


@bot.callback_query_handler(func=lambda call: call.data == 'minutes')
def minutes_increment(call):
    global hours, minutes
    minutes += 5
    if minutes >= 60:
        minutes -= 60  # обнуление счетчика
    bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                  message_id=call.message.message_id,
                                  reply_markup=create_watch(hours, minutes))


@bot.callback_query_handler(func=lambda call: call.data == 'minut_dec')
def minut_decrement(call):
    global hours, minutes
    minutes -= 10
    if minutes < 0:
        minutes += 60  # обнуление счетчика
    bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                  message_id=call.message.message_id,
                                  reply_markup=create_watch(hours, minutes))


@bot.callback_query_handler(func=lambda call: call.data == 'ignore')
def ignore(call):
    bot.answer_callback_query(call.id, text="")


bot.polling(none_stop=True, interval=0)
#TODO Додати опис замітки
#Зробити реліз (Залити на серв щоб замовник зміг затестити прогу)
#подумати чи потрібно при натискані на кнопки ховати клавіатуру
#реалізувати додавання заміток до рабочие
# домашние
# другие
#Опис до заміток при натисканні на замітку
#в меню налаштувань змінити пояс
#додати появлення в срочних заміток
#В другие добавить кнопку создать группу
#В группе додати кнопку создати замітку
#Додати emoji
#Перевірити global у всіх функціях
#Перевірити мову у всіх функціях
#Очистку данных при комманде stop
#Отменна при создании заметки
#Замінити chat на from_user
#Функцію скидання налаштувань
#Дата создания заметки
#При закінченні введення опису замітки виводити замітку і питати чи дійсно ви хочете її додати
#При введенні замітки реалізувати можливість пропустити
#виводити не 0 а 00
#Якщо до дати спрацювання замітки залишилось пару днів то виводити дату спрацювання замітки
#Якщо до дати спрацювання замітки в цей день то виводити годину:хвилину спрацювання
#Перевірити на баги якщо викликається workers а дата не введена