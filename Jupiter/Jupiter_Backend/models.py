# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ForecastHour(models.Model):
    pk_forecast_hour_id = models.AutoField(db_column='PK_forecast_hour_ID', primary_key=True)  # Field name made lowercase.
    fk_timestamp = models.ForeignKey('Forecast_Request', models.DO_NOTHING, db_column='FK_timestamp', blank=True, null=True)  # Field name made lowercase.
    timestamphour = models.IntegerField(db_column='timestamphour')
    temperature = models.IntegerField(db_column='Temperature')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forecast_hour'


class Forecast_Request(models.Model):
    pk_timestamp = models.IntegerField(db_column='PK_timestamp', primary_key=True)  # Field name made lowercase.
    currenttemperature = models.IntegerField(db_column='CurrentTemperature')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forecast_request'
