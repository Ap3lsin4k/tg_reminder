#!/usr/bin/python3
import telebot
from telebot import types
import datetime
from time_calendar import create_calendar, create_watch

bot = telebot.TeleBot("452392048:AAGOkGolzBQ-kAcgPNurmjQYyIk-cnK8GSE")
current_shown_dates = {}
global hours, minutes


@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    global hours, minutes
    hours, minutes = 12, 0
    now = datetime.datetime.now()  # Current date
    chat_id = message.chat.id
    date = (now.year, now.month)
    current_shown_dates[chat_id] = date  # Saving the current date in a dict
    markup = create_calendar(now.year, now.month)
    bot.send_message(message.chat.id, "Please, choose a date", reply_markup=markup)
    markup = create_watch(hours, minutes)
    bot.send_message(message.chat.id, "Chose hourse", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
def get_day(call):
    print(call.data, call)
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if (saved_date is not None):
        day = call.data[13:]
        date = datetime.datetime(int(saved_date[0]), int(saved_date[1]), int(day), 0, 0, 0)
        bot.send_message(chat_id, str(date))
        bot.answer_callback_query(call.id, text="")

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
