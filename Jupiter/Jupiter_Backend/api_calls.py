# from .models import Forecast_Request

import datetime
import json
import time
import requests

# Wichtig! Ohne diesen wird kein Zugirff erlaubt
apiKey = "C6KzQwff39MA8kV1"


# Server adress und port
server = "http://localhost:8000"

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
    make API call to pirateweather historic, forcast for latitude and longitude
    -> return response as json
    :return:
    """
    return requests.get(f"https://timemachine.pirateweather.net/forecast/{apikey}/{lat},{long},{time}?units=si").json()

def save_hisotric(apiKey, lat, long, time):
    """
    save hisotric forecast

    converts timestamp to 00:00 of date
        -> API Call to Pirateweather timemachine
            -> hourly Forecast from 00:00 of date
    save to db afterwards

    if no data is availabe for given time and date -> save current data in vienna instead
        -> manuell calculation of timestamp

    if data < 1970 ->  crash

    :param apiKey: Pirateweather API key
    :param lat: latitude
    :param long: longitude
    :param time: unix timestmap on given day
    :return
    """

    historic_date = datetime.datetime.fromtimestamp(time)
    historic_date = historic_date.replace(hour=0, minute=0, second=0, microsecond=0)
    historic_date = datetime.datetime.timestamp(historic_date)

    pk = int(time) + int(lat*100000) + int(long*100000)

    hisotric_forecast = {
        "pk_forecast_id": pk,
        "pk_timestamp": time,
        "currenttemperature":  12,
        "latitude": lat,
        "longitude": long
    }

    requests.post(f"{server}/api/Forecast_Request/", json=hisotric_forecast)

    hisotric_hours = []

    try:
        hisotric_forecast_data = get_hisoric_foreast_json(apiKey,lat,long,time)['hourly']['data']
    except:
        print("ERROR, no data available for this time and place -> using current forecast for vienna instead")
        hisotric_forecast_data = get_forecast_json(apiKey,lat,long)['hourly']['data']


    h = 0

    for hour in hisotric_forecast_data:

        if h > 23:
            break

        hour_time_unix = historic_date + h*3600
        #hour_time_unix = hour["time"]
        hour_time_sql = convert_timestamp_normaltime(hour_time_unix)

        hisotoric_hour = {
            "fk_request": int(pk),
            "timestamphour": hour_time_unix,
            "temperature_cur": int(hour["temperature"]),
            "humidity":  12,
            "windspeed": float(hour["windSpeed"]),
            "uvindex": 12,
            "airpressure": int(hour["pressure"]),
            "weathersummary": hour["summary"],
            "normaltime": hour_time_sql
        }

        hisotric_hours.append(hisotoric_hour)

        h+=1

    requests.post(f"{server}/api/Forecast/", json=hisotric_hours)


def save_forecast(forecast):
    """
    save forecast to database
    :param forecast: forecast
    :return: transmitted data
    """

    t = int(time.time())

    pk =  int(t) + int(forecast["latitude"]*1000) +  int(forecast["longitude"]*1000)

    forecast_request = {
        "pk_forecast_id": pk,
        "pk_timestamp": t,
        "currenttemperature": int (forecast["currently"]["temperature"]),
        "latitude": float(forecast["latitude"]),
        "longitude": float(forecast["longitude"])
    }

    requests.post(f"{server}/api/Forecast_Request/", json=forecast_request)

    forcast_hours = []

    c = 0

    for h in forecast["hourly"]["data"]:
        c += 1
        if c > 24:
            break

        forecast_hour = {
            "fk_request": pk,
            "timestamphour": int(h["time"]),
            "temperature_cur": int (h["temperature"]),
            "humidity":  float(h["humidity"]),
            "windspeed": float(h["windSpeed"]),
            "uvindex": int(h["uvIndex"]),
            "airpressure": int(h["pressure"]),
            "weathersummary": h["summary"],
            "normaltime": convert_timestamp_normaltime(int(h["time"]))
        }


        forcast_hours.append(forecast_hour)
        #print(requests.post(f"{server}/api/Forecast/", json=forecast_hour))


    requests.post(f"{server}/api/Forecast/", json=forcast_hours)

    #return forecast_request, forcast_hours


def convert_timestamp_normaltime(t):
    """
    converts unix timestamp to sql timestamp, removes date
    :param t: unix timestamp
    :return: sql timestamp only with hour and minute
    """
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
    float float int or
    float float string
    """
    if time == "now":
        return save_forecast(get_forecast_json(apiKey, lat, long))
    return save_hisotric(apiKey, lat, long, time)



#print(save_forecast(get_forecast_json(apiKey, "48.210033", "16.363449")))

#print(getandsave(48.21003,16.363449,1580336426))

#getandsave(48.210033,16.363449,"now")
