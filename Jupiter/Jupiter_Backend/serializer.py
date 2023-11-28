from rest_framework import serializers
from .models import ForecastHour, ForecastRequest

class ForecastHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastHour
        fields = ['pk_forecast_hour_id', 'fk_timestamp', 'timestamphour', 'temperature_cur', 'temperature_min', 'temperature_max', 'humidity', 'windspeed', 'uvindex', 'airpressure', 'weathersummary', 'normaltime']


class ForecastRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastRequest
        fields = ["pk_timestamp", 'latitude', 'longitude', "currenttemperature"]

