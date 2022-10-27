import sqlite3
import telebot

import os
import random

from telebot import types

TOKEN = os.getenv('TELE_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Создаем соединение с БД
connection = sqlite3.connect('db.sqlite3', check_same_thread=False)
# Курсор это обьект который делает запросы и получает из результаты
cursor = connection.cursor()


def db_table_val(username, user_id):
    pass

    cursor.execute('INSERT INTO core_user (username, user_id) VALUES (?, ?)', (username, user_id))
    connection.commit()
    # connection.close()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_add = types.KeyboardButton("Добавь меня в базу!")
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Начать чаепитие ☕️")
    help_btn = telebot.types.KeyboardButton("/help")
    markup.add(btn1, btn2, btn_add, help_btn)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот, который рандомно выберет тебе собеседника для совместного чаепития".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Добавь меня в базу!":
        bot.send_message(message.from_user.id, "Привет! Ваше имя добавлено в базу данных!")
        us_name = message.from_user.username
        # us_sname = message.from_user.last_name
        us_id = message.from_user.id

        db_table_val(username=us_name, user_id=us_id)
    elif message.text == "👋 Поздороваться":
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что ты с нами!)")
    elif message.text == "Начать чаепитие ☕️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tea = telebot.types.KeyboardButton("Пора пить чай!")
        start_btn = telebot.types.KeyboardButton("/start")
        markup.add(tea, start_btn)
        bot.send_message(message.chat.id, 'Нажми кнопку "Пора пить чай!", и я тебе отправлю имя твоего собеседника! '
                                          '\n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)
    elif message.text == "Пора пить чай!":
        # Делаем запрос к БД
        cursor.execute("SELECT username FROM core_user")
        # Получаем результат запроса
        results = cursor.fetchone()
        results != 'username'
        # connection.close()
        bot.send_message(message.from_user.id, random.choice(results))

    elif message.text == "/help":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как тебя зовут?")
        btn2 = types.KeyboardButton("Что ты можешь?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что ты можешь?":
        bot.send_message(message.chat.id, text="Выбрать тебе собеседника ☕️")

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("Начать чаепитие ☕️")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован..")


# connection.close()

bot.polling(none_stop=True)
