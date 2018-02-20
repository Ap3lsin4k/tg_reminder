# -*- coding: utf-8 -*-
import telebot
import constans

global group
group = ['Группа 1', 'Группа 2', 'Группа 3', 'Группа 4', 'Группа 5','Группа 6', 'Группа 7', 'Группа 8']
bot = telebot.TeleBot(constans.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(False, True)
    # for i in range(len(group)):
    #     user_markup.row(group[i])
    for i in range(0, len(group), 2):
        # if (i+2) < len(group):
        #     user_markup.row(group[i], group[i+1], group[i+2])
        if (i+1) < len(group):
            user_markup.row(group[i], group[i+1])
        else:
            user_markup.row(group[i])
    user_markup.row('Добавить группу', 'Назад')
    # user_markup.row('Группа 1', 'Группа 2')
    # user_markup.row('Группа 3', 'Группа 4')
    # user_markup.row('Группа 5', 'Группа 6')
    # user_markup.row('Группа 7')

    # user_markup.row('Группа 1')
    # user_markup.row('Группа 2')
    # user_markup.row('Группа 3')
    # user_markup.row('Группа 4')
    # user_markup.row('Группа 5')
    # user_markup.row('Группа 6')
    # user_markup.row('Группа 7')
    # user_markup.row('Группа 1', 'Группа 2', 'Группа 3', 'Группа 4', 'Группа 5', 'Группа 6', 'Группа 7', 'Группа 8', 'Группа 9', 'Группа 10', 'Группа 11', 'Группа 12')
    # user_markup.row('Группа 13', 'Группа 14', 'Группа 15', 'Группа 16', 'Группа 17', 'Группа 18', 'Группа 19', 'Группа 20')

    bot.send_message(message.from_user.id, '.', reply_markup=user_markup)

bot.polling(none_stop=True, interval=0)