from django.shortcuts import render
from datetime import datetime
from Jupiter_Backend.models import ForecastHour, ForecastRequest
import json

# Fick dich
icons = {
    'clear': '',
    'cloudy': '',
    'partly cloudy': '',
    'rain': '',
    'thunderstorm': '',
    'foggy': '',
    'windy': '',
    'snow': '',
    'solar-eclipse': '',
    'hail': ''
}


def index(request):
    context = {
        "currentTemp": 8,
        "wind": 0,
        "humidity": 0,
        "uv": 0,
        "pressure": 0,
        "min": 0,
        "max": 0,
        "weather": icons['clear'],
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
    print(temp)
    context['liste'] = json.dumps(temp)
    response = render(request, 'test.html', context)
    return response
