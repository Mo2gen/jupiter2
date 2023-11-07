from django.shortcuts import render
from Jupiter_Backend import api_calls

def index(request):
    context = {
        "currentTemp": 8
    }
    api_calls.getandsave()
    return render(request, 'index.html', context)