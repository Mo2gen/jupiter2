from django.shortcuts import render

def index(request):
    context = {
        "currentTemp": 8
    }
    return render(request, 'index.html', context)