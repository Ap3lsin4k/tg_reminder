# -*- coding: utf-8 -*-
import telebot
import constans

bot = telebot.TeleBot(constans.token)
current_shown_dates = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_markup = telebot.types.InlineKeyboard('asd')
    user_markup.row("hours", "min", "day", "month", "year")
    user_markup.row("12", "00", "14", "02", "2018")
    bot.send_message(message.chat.id, "Нажмите чтобы редактировать!", reply_markup=user_markup)

# @bot.message_handler(commands = ['url'])
# def url(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     btn_my_site = telebot.types.InlineKeyboardButton(text='Наш сайт')
#     markup.add(btn_my_site)
#     bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

# @bot.message_handler(commands = ['switch'])
# def switch(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     switch_button = telebot.types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
#     markup.add(switch_button)
#     bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)
#

# # Обычный режим
# @bot.message_handler(content_types=["text"])
# def any_msg(message):
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     callback_button = telebot.types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
#     keyboard.add(callback_button)
#     bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


# # Инлайн-режим с непустым запросом
# @bot.inline_handler(lambda query: len(query.query) > 0)
# def query_text(query):
#     kb = telebot.types.InlineKeyboardMarkup()
#     # Добавляем колбэк-кнопку с содержимым "test"
#     kb.add(telebot.types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
#     results = []
#     single_msg = telebot.types.InlineQueryResultArticle(
#         id="1", title="Press me",
#         input_message_content=telebot.types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
#         reply_markup=kb
#     )
#     results.append(single_msg)
#     bot.answer_inline_query(query.id, results)
#
#
# # В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     # Если сообщение из чата с ботом
#     if call.message:
#         if call.data == "test":
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
#     # Если сообщение из инлайн-режима
#     elif call.inline_message_id:
#         if call.data == "test":
#             bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")
#
# if __name__ == '__main__':
#     bot.polling(none_stop=True)

bot.polling(none_stop=True, interval=0)