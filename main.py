import telebot
from functions import get_weather_en, get_weather_ru
from constants import TOKEN, in_russian

bot = telebot.TeleBot(TOKEN, parse_mode='html')

@bot.message_handler(commands=["start"])
def start_handler(message):
    hello = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    hello.add('Select language (Выбрать язык)')
    bot.send_message(message.chat.id, f"👋 Hello, <b>{message.from_user.first_name} 👋</b>\n I'm the best weather bot :)", reply_markup=hello)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.chat.type == 'private':
        if message.text == 'Select language (Выбрать язык)' or message.text == '*Select language*' or message.text == '*Выбрать язык*':
            switch = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            switch.add(*['English 🇬🇧', 'Russian 🇷🇺'])
            bot.send_message(message.chat.id, "EN — Choose the language in menu below\nRU — Выберите язык в меню ниже", reply_markup=switch)

        elif message.text == 'Russian 🇷🇺':
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*["Вашингтон", "Москва", "Пекин", "*Выбрать язык*"])
            bot.send_message(message.chat.id, "Выберите город в меню ниже или напишите свой:", reply_markup=keyboard)
            global in_russian
            in_russian = True
                
        elif message.text == 'English 🇬🇧':
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*["Washington", "Moscow", "Pekin", "*Select language*"])
            bot.send_message(message.chat.id, "Choose a city from the menu below or type your one there:", reply_markup=keyboard)
            in_russian = False
        
        else:
            if in_russian:
                msg = get_weather_ru(message.text)
                bot.send_message(message.chat.id, msg)
            elif not in_russian:
                msg = get_weather_en(message.text)
                bot.send_message(message.chat.id, msg)
                
while True:
    try:
        if __name__ == '__main__':
            bot.polling(none_stop=True, interval=0)
    except:
        continue
