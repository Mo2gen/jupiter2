from django.db import models


class ForecastHour(models.Model):
    pk_forecast_hour_id = models.AutoField(db_column='PK_forecast_hour_ID', primary_key=True)  # Field name made lowercase.
    fk_request = models.ForeignKey('ForecastRequest', models.DO_NOTHING, db_column='FK_request', blank=True, null=True)  # Field name made lowercase.
    timestamphour = models.IntegerField(blank=True, null=True)
    temperature_cur = models.IntegerField(db_column='temperature_cur')
    humidity = models.FloatField(db_column='humidity')
    windspeed = models.FloatField(db_column='windSpeed')  # Field name made lowercase.
    uvindex = models.IntegerField(db_column='uvIndex')  # Field name made lowercase.
    airpressure = models.IntegerField(db_column='airPressure')  # Field name made lowercase.
    weathersummary = models.CharField(db_column='weatherSummary', max_length=30)  # Field name made lowercase.
    normaltime = models.TimeField(db_column='normalTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forecast_hour'


class ForecastRequest(models.Model):
    pk_forecast_id = models.AutoField(db_column='PK_forecast_ID', primary_key=True)  # Field name made lowercase.
    pk_timestamp = models.IntegerField(db_column='PK_timestamp', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    currenttemperature = models.IntegerField(db_column='CurrentTemperature')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forecast_request'
