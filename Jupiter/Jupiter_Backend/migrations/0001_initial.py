# Generated by Django 4.2.5 on 2023-11-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForecastHour',
            fields=[
                ('pk_forecast_hour_id', models.AutoField(db_column='PK_forecast_hour_ID', primary_key=True, serialize=False)),
                ('timestamphour', models.IntegerField(db_column='timestamphour')),
                ('temperature_cur', models.IntegerField(db_column='temperature_cur')),
                ('temperature_min', models.IntegerField(db_column='temperature_min')),
                ('temperature_max', models.IntegerField(db_column='temperature_max')),
                ('humidity', models.IntegerField(db_column='humidity')),
                ('windspeed', models.IntegerField(db_column='windSpeed')),
                ('uvindex', models.IntegerField(db_column='uvIndex')),
                ('airpressure', models.IntegerField(db_column='airPressure')),
                ('weathersummary', models.CharField(db_column='weatherSummary', max_length=30)),
                ('normaltime', models.TimeField(db_column='normalTime')),
            ],
            options={
                'db_table': 'forecast_hour',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForecastRequest',
            fields=[
                ('pk_timestamp', models.IntegerField(db_column='PK_timestamp', primary_key=True, serialize=False)),
                ('latitude', models.FloatField(db_column='latitude')),
                ('longitude', models.FloatField(db_column='longitude')),
                ('currenttemperature', models.IntegerField(db_column='CurrentTemperature')),
            ],
            options={
                'db_table': 'forecast_request',
                'managed': False,
            },
        ),
    ]
