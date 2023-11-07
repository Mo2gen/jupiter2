"""
Fabio Di Grillo
03.10.2023
"""

#from .models import Forecast_Request

import datetime
import time
import requests


# Wichtig! Ohne diesen wird kein Zugirff erlaubt
apiKey = "C6KzQwff39MA8kV1"

def get_forecast_json(apikey, lat, long):
    """
    make API call to pirateweather, forcast for latitude and longitude
    -> return response as json, save timestamp of request
    lat: latitude
    long: longitude
    """
    return requests.get(f"https://api.pirateweather.net/forecast/{apikey}/{lat},{long}?units=si").json()


def save_forecast(forecast):
    """



    t = Request(PK_Timestamp=time.time(),
                normaltime =convert_timestamp_normaltime(time.time()),
                CurrentTemperature = forecast["currently"]["temperature"]
                )

    t.save()
    """

    forecast_request = {
        "PK_timestamp": time.time(),
        "normaltime": convert_timestamp_normaltime(time.time()),
        "CurrentTemperature": forecast["currently"]["temperature"]
    }

    forcast_hours = []

    for h in forecast["hourly"]["data"]:
        forecast_hour = {
            "PK_timestamp": time.time(),
            "timestamphour": h["time"],
            "normaltime": convert_timestamp_normaltime(h["time"]),
            "Temperature": h["temperature"]
        }
        forcast_hours.append(forecast_hour)



        requests.post("http://127.0.0.1:6960/api/Forecast_Request/",json=requests)






    return forecast_request, forcast_hours


def convert_timestamp_normaltime(t):
    """

    """
    return datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M")



def getandsave():
    save_forecast(get_forecast_json(apiKey,41.210033,16.363449,))

print(save_forecast(get_forecast_json(apiKey, "48.210033", "16.363449")))


url = "localhost"
requests.post(f'{url}api/request/', json=data)

