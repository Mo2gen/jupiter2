from django.shortcuts import render
from datetime import datetime


def index(request):
    print(request.COOKIES.get('lang'))
    print(request.COOKIES.get('lat'))
    print(request.COOKIES.get('date'))
    context = {
        "currentTemp": 8,
        "wind": 0,
        "humidity": 0,
        "uv": 0,
        "pressure": 0,
        "min": 0,
        "max": 0,
        "weather": 'clear',
        "date": datetime.now().strftime('%A %H:%M')
    }
    response = render(request, 'test.html', context)
    return response
