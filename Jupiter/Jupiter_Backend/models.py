from django.db import models

# Create your models here.
class Request(models.Model):
    PK_Timestamp = models.IntegerField
    normaltime = models.TimeField
    CurrentTemperature = models.IntegerField


