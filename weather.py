import json

import requests


def weather(lat=None, lon=None, lang_code=None):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {
        "lat": lat,
        "lon": lon,
        "lang": lang_code,
        "units": "\"metric\" or \"imperial\"",
        "mode": "xml, html"
    }
    headers = {
        'x-rapidapi-key': "1114a2c2cdmsh9526657cb161d4bp106e3ajsndaa73de548e9",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    s = response.text
    s = json.loads(s)
    return s
