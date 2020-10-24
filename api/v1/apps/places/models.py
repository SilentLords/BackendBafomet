from django.db import models

# Create your models here.

class Place(models.Model):
    lat = models.FloatField(verbose_name='Ширина')
    lon = models.FloatField(verbose_name='Долгота')
    average_check = models.FloatField(verbose_name='Средний чек')
    id_2gis = models.CharField(max_length=40, verbose_name='ID 2GIS')