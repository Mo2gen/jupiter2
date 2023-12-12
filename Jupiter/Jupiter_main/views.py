from django.shortcuts import render
from datetime import datetime
from Jupiter_Backend.models import ForecastHour, ForecastRequest
from Jupiter_Backend.api_calls import getandsave as getandsave
import json
import math

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
    if not request.COOKIES.get('lat'):
        lat = 48.1940447
    else:
        lat = float(request.COOKIES.get('lat'))
    if not request.COOKIES.get('long'):
        long = 16.4133434
    else:
        long = float(request.COOKIES.get('long'))
    if not request.COOKIES.get('date'):
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        date = request.COOKIES.get('date')
    todayRequest = getTodayRequest(lat, long)
    today = [a for a in ForecastHour.objects.values() if a['fk_request_id'] == todayRequest['pk_forecast_id']]
    now = [a for a in today if a['normaltime'].strftime("%H") == datetime.now().strftime("%H")][0]
    context = {
        "currentTemp": now['temperature_cur'],
        "wind": round(now['windspeed'] * 3.6, 1),
        "humidity": now['humidity'] * 100,
        "uv": now['uvindex'],
        "pressure": now['airpressure'],
        "min": min([a['temperature_cur'] for a in today]),
        "max": max([a['temperature_cur'] for a in today]),
        "weather": icons[now['weathersummary'].lower()],
        "date": datetime.now().strftime('%A %H:%M'),
        'liste': dict
    }
    temp = generatelist(date, lat, long)
    context['liste'] = json.dumps(temp)
    response = render(request, 'test.html', context)
    return response


def getTodayRequest(lat: float, long: float) -> dict:
    todayRequest = None
    for a in ForecastRequest.objects.values():
        if datetime.fromtimestamp(a['pk_timestamp']).strftime("%Y-%m-%d") == datetime.now().date().strftime("%Y-%m-%d") and math.isclose(lat, a['latitude'], abs_tol=0.009) and math.isclose(long, a['longitude'], abs_tol=0.009):
            todayRequest = a
            break
    if todayRequest:
        return todayRequest
    else:
        getandsave(lat, long, "now")
        return getTodayRequest(lat, long)


def generatelist(date: str, lat: float, long: float) -> list[dict[str, Any]]:
    """
    Generiert eine Dictionary mit Daten für das Generieren des Graphen
    :param date: Datum im Jahr-Monat-Tag Format
    :param lat: Längengrad
    :param long: Breitengrad
    :return:
    """
    liste = None
    for a in ForecastRequest.objects.values():
        if date == datetime.fromtimestamp(a['pk_timestamp']).strftime("%Y-%m-%d") == datetime.now().date().strftime("%Y-%m-%d") and math.isclose(lat, a['latitude'], abs_tol=0.009) and math.isclose(long, a['longitude'], abs_tol=0.009):
            liste = [
                {
                    'timestamphour': b['timestamphour'],
                    'normaltime': b['normaltime'].strftime('%H:%M:%S'),
                    'Temperature': b['temperature_cur'],
                    'weather': icons[b['weathersummary'].lower()]
                }
                for b in ForecastHour.objects.values() if b['fk_request_id'] == a['pk_forecast_id']
            ]
    if liste:
        return liste
    else:
        getandsave(lat, long, date)
        return generatelist(date, lat, long)
