from telebot import types
from config import *

def button(*titles: str) -> object:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.max_row_keys = 3
    markup.row(*titles, '|||')
    return markup

def menu():
    return button("Who", 'Location', 'Episode')