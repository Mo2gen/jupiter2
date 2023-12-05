# from .models import Forecast_Request

import datetime
import time
import requests

# Wichtig! Ohne diesen wird kein Zugirff erlaubt
apiKey = "C6KzQwff39MA8kV1"

# Server adress und port
server = "http://localhost:80"

# michal hallo

def get_forecast_json(apikey, lat, long, time = time.time()):
    """
    make API call to pirateweather, forcast for latitude and longitude
    -> return response as json, save timestamp of request
    lat: latitude
    long: longitude
    """
    return requests.get(f"https://api.pirateweather.net/forecast/{apikey}/{lat},{long},{time}?units=si").json()

def get_hisoric_foreast_json(apikey, lat, long, time):
    """

    :return:
    """
    return requests.get(f"https://timemachine.pirateweather.net/forecast/{apikey}/{lat},{long},{time}?units=si").json()

def get_and_save_hisotric(apiKey,lat,long,time):
    """

    :param apiKey:
    :param lat:
    :param long:
    :param time:
    :return:
    """
    historic_date = datetime.datetime.fromtimestamp(time)
    historic_date = historic_date.replace(hour=0, minute=0, second=0, microsecond=0)
    historic_date = datetime.datetime.timestamp(historic_date)
    print (historic_date)

    hisotric_forecast = {
        "pk_timestamp": historic_date,
        "currenttemperature": 0,
        "latitude": lat,
        "longitude": long
    }

   # print(requests.post(f"{server}/api/Forecast_Request/", json=hisotric_forecast))

    h = historic_date
    for hour in range(24):
        print(h)
        print(datetime.datetime.fromtimestamp(h))
        print(get_hisoric_foreast_json(apiKey,lat,long,h))

        historic_hour_data = get_hisoric_foreast_json(apiKey,lat,long,time) ["currently"]

        print(historic_hour_data)

        hisotoric_hour = {
            "fk_timestamp": historic_date,
            "timestamphour": int(historic_hour_data["time"]),
            "temperature_cur": int (historic_hour_data["temperature"]),
            "humidity":  12,
            "windspeed": float(historic_hour_data["windSpeed"]),
            "uvindex": 12,
            "airpressure": int(historic_hour_data["pressure"]),
            "weathersummary": historic_hour_data["summary"],
            "normaltime": datetime.datetime.fromtimestamp(h)
        }

        print(hisotoric_hour)

        historic_date = h + 3600

      #  print(requests.post(f"{server}/api/Forecast/", json=forecast_hour))


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
            "fk_timestamp": t,
            "timestamphour": int(h["time"]),
            "temperature_cur": int (h["temperature"]),
            "humidity":  float(h["humidity"]),
            "windspeed": float(h["windSpeed"]),
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
    return get_and_save_hisotric(apiKey,lat.lat, long, time)



#print(save_forecast(get_forecast_json(apiKey, "48.210033", "16.363449")))

#print(getandsave(48.21003,16.363449,"now"))

get_and_save_hisotric(apiKey,"48.210033","16.363449",1699780703)

