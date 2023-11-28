from django.db import models


class ForecastHour(models.Model):
    pk_forecast_hour_id = models.AutoField(db_column='PK_forecast_hour_ID', primary_key=True)
    fk_timestamp = models.ForeignKey('ForecastRequest', models.DO_NOTHING, db_column='FK_timestamp', blank=True, null=True)
    timestamphour = models.IntegerField(db_column='timestamphour')
    temperature_cur = models.IntegerField(db_column='temperature_cur')
    temperature_min = models.IntegerField(db_column='temperature_min')
    temperature_max = models.IntegerField(db_column='temperature_max')
    humidity = models.IntegerField(db_column='humidity')
    windspeed = models.IntegerField(db_column='windSpeed')
    uvindex = models.IntegerField(db_column='uvIndex')
    airpressure = models.IntegerField(db_column='airPressure')
    weathersummary = models.CharField(db_column='weatherSummary', max_length=30)
    normaltime = models.TimeField(db_column='normalTime')

    class Meta:
        managed = False
        db_table = 'forecast_hour'


class ForecastRequest(models.Model):
    pk_timestamp = models.IntegerField(db_column='PK_timestamp', primary_key=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    currenttemperature = models.IntegerField(db_column='CurrentTemperature')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forecast_request'
