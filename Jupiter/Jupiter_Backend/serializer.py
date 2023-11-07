from rest_framework import serializers
from .models import ForecastHour, Forecast_Request

class ForecastHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastHour
        fields = ['pk_forecast_hour_id','fk_timestamp','timestamphour',"temperature"]


class Forecast_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast_Request
        fields = ["pk_timestamp","currenttemperature"]

