import time
from datetime import datetime

from backports.zoneinfo import ZoneInfo

import weather


def get_local_time(s):
    s = s + 18000
    today = datetime.now()
    qw = [today.year, today.month, today.day]
    ans = time.strftime('%H:%M:%S', time.gmtime(s))
    ans = qw + list(map(int, ans.split(':')))
    d = datetime(*ans, tzinfo=ZoneInfo(key='Asia/Tashkent'))
    ans = ':'.join(list(map(str, [d.hour, d.minute]))) + '  ' \
          + '-'.join(list(map(str, [d.year, d.month, d.day])))
    return ans


def get_text(message):
    lat, long = message.location.latitude, message.location.longitude
    lang_code = message.from_user.language_code
    obj = weather.weather(lat, long, lang_code)
    author = f"Thank you @{message.chat.username} for using our service\n\n"
    temp = '🌡Temperature: ' + str(int(obj['main']['feels_like']) - 273) + ' - ' + str(
        int(obj['main']['temp_max']) - 273) + '°C\n'
    wind_speed = '💨 Wind speed: ' + str(obj['wind']['speed']) + 'm/s\n\n'
    sun_rise_set = '🕔 🌖 Sunrise at ' + str(get_local_time(obj['sys']['sunrise'])) + '\n' + \
                   '🕣 🌒 Sunset at ' + str(get_local_time(obj['sys']['sunset'])) + '\n'
    addres = '📍 Addres: ' + obj['name'] + '/' + obj['sys']['country'] + '\n'
    pressure = 'Pressure: ' + str(obj['main']['pressure']) + 'mm.sim.ust\n'

    text = author + temp + wind_speed + sun_rise_set + pressure + addres + temp + wind_speed + sun_rise_set + pressure + addres
    return text
