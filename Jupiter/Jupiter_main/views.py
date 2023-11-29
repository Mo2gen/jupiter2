from django.shortcuts import render
from datetime import datetime
from Jupiter_Backend.models import ForecastHour, ForecastRequest
# from Jupiter_Backend.api_calls import getandsave
import json

# Fick dich
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
    today = [a for a in ForecastHour.objects.values() if datetime.fromtimestamp(a['fk_timestamp_id']).strftime("%Y-%m-%d") == datetime.now().date().strftime("%Y-%m-%d")]
    now = [a for a in today if a['normaltime'].strftime("%H") == datetime.now().strftime("%H")][0]
    context = {
        "currentTemp": now['temperature_cur'],
        "wind": now['temperature_cur'],
        "humidity": now['humidity'],
        "uv": now['uvindex'],
        "pressure": now['airpressure'],
        "min": int,
        "max": int,
        "weather": icons[now['weathersummary'].lower()],
        "date": datetime.now().strftime('%A %H:%M'),
        'liste': dict
    }
    temp = None
    for a in ForecastRequest.objects.values():
        if request.COOKIES.get('date') == datetime.fromtimestamp(a['pk_timestamp']).strftime("%Y-%m-%d"):
            temp = [
                {
                    'PK_timestamp': b['fk_timestamp_id'],
                    'timestamphour': b['timestamphour'],
                    'normaltime': b['normaltime'].strftime('%H:%M:%S'),
                    'Temperature': b['temperature_cur'],
                    'weather': icons[b['weathersummary'].lower()]
                }
                for b in ForecastHour.objects.values() if b['fk_timestamp_id'] == a['pk_timestamp']
            ]
    print([a['temperature_cur'] for a in today])
    context['max'] = max([a['temperature_cur'] for a in today])
    context['min'] = min([a['temperature_cur'] for a in today])
    context['liste'] = json.dumps(temp)
    response = render(request, 'test.html', context)
    return response
