# from .models import Forecast_Request

import datetime
import time
import requests

# Wichtig! Ohne diesen wird kein Zugirff erlaubt
apiKey = "C6KzQwff39MA8kV1"

# Server adress und port
server = "http://localhost:9000"

# michal hallo

def get_forecast_json(apikey, lat, long, time = time.time()):
    """
    make API call to pirateweather, forcast for latitude and longitude
    -> return response as json, save timestamp of request
    lat: latitude
    long: longitude
    """
    return requests.get(f"https://api.pirateweather.net/forecast/{apikey}/{lat},{long},{time}?units=si").json()



def save_forecast(forecast):
    """
    save forecast to database
    :param forecast: forecast
    :return: transmitted data
    """
    print(forecast)
    t = int(time.time())
    forecast_request = {
        "pk_timestamp": t,
        "currenttemperature": int (forecast["currently"]["temperature"]),
        "latitude": float(forecast["latitude"]),
        "longitude": float(forecast["longitude"])
    }
    print(forecast_request)

    print(requests.post(f"{server}/api/Forecast_Request/", json=forecast_request))

    forcast_hours = []

    c = 0

    for h in forecast["hourly"]["data"]:
        c += 1
        if c > 24:
            break

        forecast_hour = {
            "fk_timestamp" : t,
            "timestamphour" : int(h["time"]),
            "temperature_cur" : int (h["temperature"]),
            "temperature_min": 12,# int(h["temepratureMin"]),
            "temperature_max": 12,#int(h["temepratureMax"]),
            "humidity" :  int(h["humidity"]),
            "windspeed" : int(h["windSpeed"]),
            "uvindex": int(h["uvIndex"]),
            "airpressure": int(h["pressure"]),
            "weathersummary": h["summary"],
            "normaltime": convert_timestamp_normaltime(int(h["time"]))
        }

        print(forecast_hour)
        forcast_hours.append(forecast_hour)
        print(requests.post(f"{server}/api/Forecast/", json=forecast_hour))

    return forecast_request, forcast_hours


def convert_timestamp_normaltime(t):
    return datetime.datetime.fromtimestamp(t).strftime("%H:%M")


def getandsave(lat,long, time):
    """
    get weather data from weather pirates and save to db

    :param lat: latitude
    :param long: longitude
    :param time: time of forecast, if time = now -> now
    :return: output of save forecast function

    example:
    print(getandsave(48.21003,16.363449,"now"))
    """
    if time == "now":
        return save_forecast(get_forecast_json(apiKey, lat, long))
    return save_forecast(get_forecast_json(apiKey, lat, long,time))



#print(save_forecast(get_forecast_json(apiKey, "48.210033", "16.363449")))

print(getandsave(48.21003,16.363449,"now"))