from django.shortcuts import render
from Jupiter_Backend import api_calls
from datetime import datetime

def index(request):
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
    return render(request, 'test.html', context)