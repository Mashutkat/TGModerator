import telebot
from telebot import types
import time

# Вставьте токен своего бота
bot = telebot.TeleBot('TOKEN')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот, который может блокировать, кикать, мутить и размутить пользователей в чате. Для использования моих функций, вы должны быть администратором чата.")

# Обработчик команды /ban
@bot.message_handler(commands=['ban'])
def ban(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "Пользователь заблокирован.")
    else:
        bot.reply_to(message, "Вы должны ответить на сообщение пользователя, которого хотите заблокировать.")

# Обработчик команды /mute
@bot.message_handler(commands=['mute'])
def mute(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        duration = int(message.text.split()[1])
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
        bot.reply_to(message, f"Пользователь замучен на {duration} секунд.")
        time.sleep(duration)
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True)
        bot.reply_to(message, "Мут пользователя снят.")
    else:
        bot.reply_to(message, "Вы должны ответить на сообщение пользователя, которого хотите замутить, и указать время в секундах.")

# Обработчик команды /unmute
@bot.message_handler(commands=['unmute'])
def unmute(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True)
        bot.reply_to(message, "Мут пользователя снят.")
    else:
        bot.reply_to(message, "Вы должны ответить на сообщение пользователя, которого хотите размутить.")

# Обработчик команды /kick
@bot.message_handler(commands=['kick'])
def kick(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "Пользователь кикнут.")
    else:
        bot.reply_to(message, "Вы должны ответить на сообщение пользователя, которого хотите кикнуть.")

# Обработчик команды /unban
@bot.message_handler(commands=['unban'])
def unban(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.unban_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "Пользователь разблокирован.")
    else:
        bot.reply_to(message, "Вы должны ответить на сообщение пользователя, которого хотите разблокировать.")

# Запуск бота
bot.polling()