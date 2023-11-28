from django.shortcuts import render
from datetime import datetime
from Jupiter_Backend.models import ForecastHour, ForecastRequest
icons = {
    'clear': '',
    'cloudy': '',
    'rain': '',
    'thunderstorm': '',
    'foggy': '',
    'windy': '',
    'snowing': '',
    'solar-eclipse': ''
}

def index(request):
    print(request.COOKIES.get('long'))
    print(request.COOKIES.get('lat'))
    print(request.COOKIES.get('date'))
    for a in ForecastRequest.objects.values():
        print(a)
        print(datetime.fromtimestamp(a['pk_timestamp']).date())
        if request.COOKIES.get('date') == datetime.fromtimestamp(a['pk_timestamp']).date():
            print('found!!!!!!!!!!!!!!!!!!')
    context = {
        "currentTemp": 8,
        "wind": 0,
        "humidity": 0,
        "uv": 0,
        "pressure": 0,
        "min": 0,
        "max": 0,
        "weather": icons['clear'],
        "date": datetime.now().strftime('%A %H:%M')
    }
    response = render(request, 'test.html', context)
    return response
