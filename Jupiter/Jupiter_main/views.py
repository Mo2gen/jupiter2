from django.template import loader
from django.shortcuts import render
from Jupiter_Backend import api_calls

def index(request):
    context = {
        "currentTemp": 833
    }
    api_calls.test()
    return render(request, 'index.html', context)