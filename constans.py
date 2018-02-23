token = "528577755:AAH7P2SLePBH183CYGJUrzEmbCYKC9CWX4Q" # @rem57
#token = "543322633:AAEg7Gn7bP4Y7Qg2kkDPUbwz2kozxwd-DUc" #  @optimizer_bot
"""
import telebot

import constants

bot = telebot.TeleBot(constants.token)

#upd = bot.get_updates()
#print (upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(bot.get_me())

def log(message,answer):
    print("/n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))


@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Мои возможности ограничены. Sorry!"
    log(message, answer)
    bot.send_message(message.chat.id, answer )

@bot.message_handler(commands=['start'])
def handle_text(message):
    answer = "Hello! You are welcome!"
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['settings'])
def handle_text(message):
    answer = "Тут пусто)"
    log(message, answer)
    bot.send_message(message.chat.id,answer )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты поц, гыгы"
    if message.text == "a":
        answer = "АУЕ"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "e":
        answer = "Ты лол"
        log(message, answer)
        bot.send_message(message.chat.id,answer)
    else:
        log(message, answer)
        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)﻿
"""
#
# {'game_short_name': None, 'chat_instance': '-2965025759710504744', 'id': '2023461295306177457', 'from_user': {'id': 471123795, 'is_bot': False, 'first_name': 'Andrii', 'username': 'ju57man', 'last_name': 'Fedorko', 'language_code': 'uk'}, 'message': {'content_type': 'text', 'message_id': 1731, 'from_user': <telebot.types.User object at 0x0534E990>, 'date': 1518634591, 'chat': <telebot.types.Chat object at 0x0534E670>, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Please, choose a date', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None}, 'data': 'calendar-day-22', 'inline_message_id': None}
