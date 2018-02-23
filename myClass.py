import telebot
import datetime
from time_calendar import create_calendar, create_watch

class NOTE:

    def __init__(self, name_button):
        self.some_group = {}
        self.edit_note_work = ""
        self.current_shown_dates = {}  # зберігає дату користувача під ключем = [message.from_user.id]

        now = datetime.datetime.now()
        #self.time = {'year': now.year, 'month': now.month, 'day': now.day,
        #            'hour': 12, 'minute': 0}  # delete


    def add_note(self, bot, message, lang):
        hide_markup = telebot.types.ReplyKeyboardRemove()
        if lang == 'ru':
            bot.send_message(message.from_user.id, "Введите название заметки", reply_markup=hide_markup)
        else:
            bot.send_message(message.from_user.id, "Enter a note name", reply_markup=hide_markup)
        # якщо ми не пишемо self. то змінна буде локальною, і видалиться при завершенні функції
        # self.time = {'year': None, 'month': None, 'day': None,
        #              'hour': None, 'minute': None}  # delete

    def add_note_name(self, message_text):  # handle note name
        self.edit_note_work = message_text  # {('назва замітки') яка вказує (:), на словник параметрів замітки {'time': '...', 'descript': '...'}}
        self.some_group[self.edit_note_work] = {'time': {'year': None, 'month': None, 'day': None, 'hour': 12, 'minute': 0},
                                                'description': ""}

    def add_note_day(self, bot, message, lang):  # handle day note
        self.some_group[self.edit_note_work]['time'] = self.time  # {'year': , 'month': , 'day': , ...}
        pass

    def add_note_time(self, bot, message, lang):  # вибрали дату і час нажавши на ОК
        #self.some_group[self.edit_note_work]['time'] = self.time

        #for next
        if lang == 'ru':
            bot.send_message(message.from_user.id, "Введите описание заметки")
        else:
            bot.send_message(message.from_user.id, "Enter a note description")
        pass

    def add_note_description(self, message):
        self.some_group[self.edit_note_work]['description'] = message.text
        self.edit_note_work = ""  # для Debug

    def main(self, bot, message, lang):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        for name_note in self.some_group:
            if name_note != "":  # для Debug
                format_date = str(self.some_group[name_note]['time']['hour']) + ":" \
                              + str(self.some_group[name_note]['time']['minute']) + "\n" \
                            + str(self.some_group[name_note]['time']['day']) + "." \
                            + str(self.some_group[name_note]['time']['month']) + "." \
                              + str(self.some_group[name_note]['time']['year'])

                user_markup.row(name_note, self.some_group[name_note]['description'],  format_date, )  # Вивести замітку і гарно відформатований час       18:36
        # print("::::", self.some_group)
        if lang == 'ru':
            user_markup.row('Добавить заметку', 'Назад')
            bot.send_message(message.from_user.id, "Нажмите на заметку, чтобы её отредактировать",
                             reply_markup=user_markup)
        else:
            user_markup.row('Add note', 'Back')
            bot.send_message(message.from_user.id, "Click on a note to edit it", reply_markup=user_markup)

# calendar handle
    # inline create
    def get_calendar(self, bot, message, lang):
        self.some_group[self.edit_note_work]['time']['hour'] = 12
        self.some_group[self.edit_note_work]['time']['minute'] = 0 # Стандартні параметри

        now = datetime.datetime.now()  # Current date
        self.current_shown_dates[message.from_user.id] = (now.year, now.month)  #

        markup = create_calendar(now.year, now.month)  # створюємо inline calendar з поточною датою

        if lang == 'ru':
            bot.send_message(message.chat.id, "Выберите дату", reply_markup=markup)  # виводимо календар
        else:
            bot.send_message(message.chat.id, "Please, choose a date", reply_markup=markup)  # виводимо календар

    # inline handle
    def get_day(self, bot, call, location, lang):
        chat_id = call.message.chat.id
        # myClass.work.current_shown_dates.get(chat_id)
        saved_date = self.current_shown_dates.get(chat_id)
        if (saved_date is not None):
            day = call.data[13:]  # день на который нажал юзер
            date = datetime.datetime(int(saved_date[0]), int(saved_date[1]), int(day), self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute'])
            self.some_group[self.edit_note_work]['time']['year'] = str(saved_date[0])
            self.some_group[self.edit_note_work]['time']['month'] = str(saved_date[1])
            self.some_group[self.edit_note_work]['time']['day'] = str(day)
            bot.send_message(chat_id, str(date))
            bot.answer_callback_query(call.id, text="")

            if location[1] == 'add_note_time1':
                location[1] = 'add_note_time2'
                # get_watch()
                if lang == 'ru':
                    bot.send_message(call.from_user.id, "Выберете время", reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute']))
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                    user_markup.row("Дальше")
                    bot.send_message(call.from_user.id, "И нажмите на кнопку \"Дальше\"", reply_markup=user_markup)
                else:
                    bot.send_message(call.from_user.id, "Select the time", reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute']))
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                    user_markup.row("OK")
                    bot.send_message(call.from_user.id, "And click on the button \"OK\"", reply_markup=user_markup)
        else:
            # Do something to inform of the error
            pass
        return location


    def next_month(self, bot, call, lang):
        chat_id = call.message.chat.id
        saved_date = self.current_shown_dates.get(chat_id)
        if saved_date is not None:
            self.some_group[self.edit_note_work]['time']['year'] = saved_date[0]
            self.some_group[self.edit_note_work]['time']['month'] = saved_date[1] + 1  # Додаємо 1 місяць

            if self.some_group[self.edit_note_work]['time']['month'] > 12:
                self.some_group[self.edit_note_work]['time']['month'] -= 12
                self.some_group[self.edit_note_work]['time']['year'] += 1
            self.current_shown_dates[chat_id] = (self.some_group[self.edit_note_work]['time']['year'], self.some_group[self.edit_note_work]['time']['month'])
            markup = create_calendar(self.some_group[self.edit_note_work]['time']['year'], self.some_group[self.edit_note_work]['time']['month'])
            if lang == 'ru':
                bot.edit_message_text("Выберите дату", call.from_user.id, call.message.message_id,
                                      reply_markup=markup)
            else:
                bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id,
                                      reply_markup=markup)
            bot.answer_callback_query(call.id, text="")
        else:
            # Do something to inform of the error
            pass

    def previous_month(self, bot, call, lang):
        chat_id = call.message.chat.id
        saved_date = self.current_shown_dates.get(chat_id)
        if saved_date is not None:
            self.some_group[self.edit_note_work]['time']['year'] = saved_date[0]
            self.some_group[self.edit_note_work]['time']['month'] = saved_date[1] - 1 # Віднімаємо місяць
            if self.some_group[self.edit_note_work]['time']['month'] < 1:
                self.some_group[self.edit_note_work]['time']['month'] += 12  # Місяць стає груднем
                self.some_group[self.edit_note_work]['time']['year'] -= 1  # Рік стає попереднім
            self.current_shown_dates[chat_id] = (self.some_group[self.edit_note_work]['time']['year'], self.some_group[self.edit_note_work]['time']['month'])
            markup = create_calendar(self.some_group[self.edit_note_work]['time']['year'], self.some_group[self.edit_note_work]['time']['month'])
            if lang == 'ru':
                bot.edit_message_text("Выберите дату", call.from_user.id, call.message.message_id,
                                      reply_markup=markup)
            else:
                bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id,
                                      reply_markup=markup)
            bot.answer_callback_query(call.id, text="")
        else:
            # Do something to inform of the error
            pass


    def hours_increment(self, bot, call):
        self.some_group[self.edit_note_work]['time']['hour'] += 1
        if self.some_group[self.edit_note_work]['time']['hour'] >= 24:  # 0 -> ... -> 23 -> 0
            self.some_group[self.edit_note_work]['time']['hour'] -= 24

        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute'])
                                      )

    def hours_decrement(self, bot, call):
        self.some_group[self.edit_note_work]['time']['hour'] -= 1
        if self.some_group[self.edit_note_work]['time']['hour'] < 0:  # 0 -> ... -> 23 -> 0
            self.some_group[self.edit_note_work]['time']['hour'] += 24
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute']))


    def minut_increment(self, bot, call):
        self.some_group[self.edit_note_work]['time']['minute'] += 10
        if self.some_group[self.edit_note_work]['time']['minute'] >= 60:
            self.some_group[self.edit_note_work]['time']['minute'] -= 60  # обнуление счетчика
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute']))

    def minutes_increment(self, bot, call):
        self.some_group[self.edit_note_work]['time']['minute'] += 5
        if self.some_group[self.edit_note_work]['time']['minute'] >= 60:
            self.some_group[self.edit_note_work]['time']['minute'] -= 60  # обнуление счетчика
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute']))

    def minut_decrement(self, bot, call):
        self.some_group[self.edit_note_work]['time']['minute'] -= 10
        if self.some_group[self.edit_note_work]['time']['minute'] < 0:
            self.some_group[self.edit_note_work]['time']['minute'] += 60  # обнуление счетчика
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=create_watch(self.some_group[self.edit_note_work]['time']['hour'], self.some_group[self.edit_note_work]['time']['minute'])
                                      )


    def ignore(self, bot, call):
        bot.answer_callback_query(call.id, text="")


work = NOTE("WORKERS")
home = NOTE("HOME")
urgent = NOTE("URGENT")