from django.template import loader
from django.shortcuts import render


def index(request):
    context = {
        "currentTemp": 833
    }
    return render(request, 'index.html', context)