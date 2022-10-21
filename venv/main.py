import sqlite3
import telebot

import os
import random

from telebot import types

TOKEN = os.getenv('TELE_TOKEN')
bot = telebot.TeleBot(TOKEN)
companion = ['Аня', 'Павел', 'Анастасия', 'Григорий', 'Азамат', 'Денис', 'Алия']

#from django.db import models

# Create your models here.
# class Article(models.Model):
# article_title=models.CharField('Название статьи',max_length=200)
# article_text=models.TextField('Текст статьи')
# pub_date=models.DateTimeField('Дата публикации')
# class Comment(models.Model):
# article=models.ForeignKey(Article,on_delete=models.CASCADE)
# author_name=models.CharField('Имя автора',max_length=50)
# comment_text=models.CharField('Текст комментария',max_length=200)

# conn = sqlite3.connect('share/main.py', check_same_thread=False)
# cursor = conn.cursor()
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
#
#         us_id = message.from_user.id
#         us_name = message.from_user.first_name
#         us_sname = message.from_user.last_name
#         username = message.from_user.username
#
#         db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

# def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
# 	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
# 	conn.commit()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Начать чаепитие ☕️")
    help_btn = telebot.types.KeyboardButton("/help")
    markup.add(btn1, btn2, help_btn)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который рандомно выберет тебе собеседника для совместного чаепития".format(
                         message.from_user), reply_markup=markup)

connection = sqlite3.connect('User.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User
              (Name TEXT, Surname TEXT, ID INT)''')
connection.commit()
connection.close()

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что ты с нами!)")
    elif (message.text == "Начать чаепитие ☕️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tea = telebot.types.KeyboardButton("Пора пить чай!")
        start = telebot.types.KeyboardButton("/start")
        markup.add(tea, start)
        bot.send_message(message.chat.id, 'Нажми кнопку "Пора пить чай!", и я тебе отправлю имя твоего собеседника! \n А если хочешь вернуться в меню нажми "start"',
                         reply_markup=markup)
    elif (message.text == "Пора пить чай!"):
        bot.send_message(message.chat.id, random.choice(companion))

    elif (message.text == "/help"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как тебя зовут?")
        btn2 = types.KeyboardButton("Что ты можешь?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как тебя зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что ты можешь?":
        bot.send_message(message.chat.id, text="Выбрать тебе собеседника ☕️")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("Начать чаепитие ☕️")
        button3 = types.KeyboardButton("/help")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


bot.polling(none_stop=True)
