import telebot

import weather
from utils import get_local_time

TOKEN = ""
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Hello @{message.chat.username}  please send me your location'
    )


@bot.message_handler(content_types=['location'])
def handle_location(message):
    lat, long = message.location.latitude, message.location.longitude
    lang_code = message.from_user.language_code
    obj = weather.weather(lat, long, lang_code)
    author = f"Thank you @{message.chat.username} for using our service\n\n"
    temp = '๐กTemperature: ' + str(int(obj['main']['feels_like']) - 273) + ' - ' + str(
        int(obj['main']['temp_max']) - 273) + 'ยฐC\n'
    wind_speed = '๐จ Wind speed: ' + str(obj['wind']['speed']) + 'm/s\n\n'
    sun_rise_set = '๐ ๐ Sunrise at ' + str(get_local_time(obj['sys']['sunrise'])) + '\n' + \
                   '๐ฃ ๐ Sunset at ' + str(get_local_time(obj['sys']['sunset'])) + '\n'
    addres = '๐ Addres: ' + obj['name'] + '/' + obj['sys']['country'] + '\n'
    pressure = 'Pressure: ' + str(obj['main']['pressure']) + 'mm.sim.ust\n'

    text = author + temp + wind_speed + sun_rise_set + pressure + addres
    print('Succes')
    bot.send_message(
        chat_id=message.chat.id,
        text=text
    )


bot.polling()
