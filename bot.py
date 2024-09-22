import telebot # библиотека telebot
from config import token # импорт токена

bot = telebot.TeleBot(token) 
mute = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    chat_id = message.chat.id # сохранение id чата
    user_id = message.reply_to_message.from_user.id
    user_id1 = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status 
    user_status1 = bot.get_chat_member(chat_id, user_id1).status 
    if message.reply_to_message and (user_status1 == 'administrator' or user_status1 == 'creator'): #проверка на то, что эта команда была вызвана в ответ на сообщение 
       
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")


@bot.message_handler(commands=['mute'])
def mute_user(message):
    chat_id = message.chat.id # сохранение id чата
    user_id1 = message.reply_to_message.from_user.id
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status 
    if message.reply_to_message and (user_status == 'administrator' or user_status == 'creator'):
        mute.append(user_id1)





@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    chat_id = message.chat.id 
    user_id = message.from_user.id
    user_status = bot.get_chat_member(chat_id, user_id).status
    if "https://" in message.text:
       
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.from_user.username} был забанен.")
    elif user_id in mute:
        bot.delete_message(message.chat.id, message.message_id)



bot.infinity_polling(none_stop=True)
