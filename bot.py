import telebot
import time
from config import *
from main import button, menu
from locat import get_location_text, get_location_names
from character import get_character_text, get_character_names
from episo import get_episode_text, get_episode_names

DATA = {}
bot = telebot.TeleBot(BOT_API)

def user(message):
    last_name = message.from_user.last_name if message.from_user.last_name is not None else ''
    first_name = message.from_user.first_name if message.from_user.first_name is not None else ''
    text = message.text
    id_ = message.from_user.id
    data = time.ctime(message.date)
    print(f'Name: {first_name, last_name}, id: {id_}, data: {data}, text_user: {text}')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEJOpJkfzlxQ-oaO83GFmVge_ZjFLgrVAAC7VsBAAFji0YMzeH62M2yzfovBA')
    bot.send_message(message.chat.id, "Select button", reply_markup=menu())
    user(message)
    
@bot.message_handler(content_types=['text'])
def main_handler(message):
    if message.chat.type == "private":
        if message.text == "Who":
            markup = button(*get_character_names())
            bot.send_message(message.chat.id, "Say character name", reply_markup=markup)
            DATA['d'] = "Who"

        elif message.text == "Location":
            markup = button(*get_location_names())
            bot.send_message(message.chat.id, "Say location name", reply_markup=markup)
            DATA["d"] = "Location"

        elif message.text == "Episode":
            markup = button(*get_episode_names())
            bot.send_message(message.chat.id, "Say episode name", reply_markup=markup)  
            DATA["d"] = "Episode"

        elif message.text != '|||':

            if DATA["d"] == "Episode":
                bot.send_message(message.chat.id, get_episode_text(message.text))

            elif DATA["d"] == "Location":
                bot.send_message(message.chat.id, get_location_text(message.text))

            elif DATA["d"] == "Who":
                bot.send_message(message.chat.id, get_character_text(message.text))

        elif message.text == '|||':
            bot.send_message(message.chat.id, "Select button", reply_markup=menu())
    user(message)

bot.polling(non_stop=True)