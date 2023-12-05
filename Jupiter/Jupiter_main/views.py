from django.shortcuts import render
from datetime import datetime
from Jupiter_Backend.models import ForecastHour, ForecastRequest
from Jupiter_Backend.api_calls import getandsave as getandsave
import json

icons = {
    'clear': '',
    'cloudy': '',
    'partly cloudy': '',
    'rain': '',
    'thunderstorm': '',
    'fog': '',
    'windy': '',
    'snow': '',
    'solar-eclipse': '',
    'hail': ''
}


def index(request):
    global todayRequest
    if not request.COOKIES.get('lat'):
        lat = 48.1940447
    else:
        lat = request.COOKIES.get('lat')
    if not request.COOKIES.get('long'):
        long = 16.4133434
    else:
        long = request.COOKIES.get('long')
    if not request.COOKIES.get('date'):
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        date = request.COOKIES.get('date')

    for a in ForecastRequest.objects.values():
        if datetime.fromtimestamp(a['pk_timestamp']).strftime("%Y-%m-%d") == datetime.now().date().strftime("%Y-%m-%d") and a['latitude'] == lat and a['longitude'] == long:
            todayRequest = a
    if not todayRequest:
        getandsave(lat, long, "now")
        for a in ForecastRequest.objects.values():
            if datetime.fromtimestamp(a['pk_timestamp']).strftime("%Y-%m-%d") == datetime.now().date().strftime("%Y-%m-%d") and a['latitude'] == lat and a['longitude'] == long:
                todayRequest = a
    today = [a for a in ForecastHour.objects.values() if a['fk_request'] == todayRequest['pk_forecast_id']]
    now = [a for a in today if a['normaltime'].strftime("%H") == datetime.now().strftime("%H")][0]
    context = {
        "currentTemp": now['temperature_cur'],
        "wind": now['windspeed'] * 3.6,
        "humidity": now['humidity'] * 100,
        "uv": now['uvindex'],
        "pressure": now['airpressure'],
        "min": min([a['temperature_cur'] for a in today]),
        "max": max([a['temperature_cur'] for a in today]),
        "weather": icons[now['weathersummary'].lower()],
        "date": datetime.now().strftime('%A %H:%M'),
        'liste': dict
    }
    temp = generatelist(date)
    if not temp:
        print(int(datetime.strptime(date, '%Y-%m-%d').timestamp()))
        #getandsave(lat, long, int(datetime.strptime(date, '%Y-%m-%d').timestamp()))
    #   temp = generatelist(date)
    context['liste'] = json.dumps(temp)
    response = render(request, 'test.html', context)
    return response


def generatelist(date: str):
    liste = None
    for a in ForecastRequest.objects.values():
        if date == datetime.fromtimestamp(a['pk_timestamp']).strftime("%Y-%m-%d"):
            liste = [
                {
                    'PK_timestamp': b['fk_timestamp_id'],
                    'timestamphour': b['timestamphour'],
                    'normaltime': b['normaltime'].strftime('%H:%M:%S'),
                    'Temperature': b['temperature_cur'],
                    'weather': icons[b['weathersummary'].lower()]
                }
                for b in ForecastHour.objects.values() if b['fk_timestamp_id'] == a['pk_timestamp']
            ]
    if liste:
        return liste
    return