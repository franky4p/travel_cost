from django.db import models

# Create your models here.

class Countries_Cities(models.Model):
    country = models.CharField("country", max_length = 100)
    city = models.CharField("city", max_length = 100)
    country_rus = models.CharField("страна", max_length = 100)
    city_rus = models.CharField("город", max_length = 100)
    airport = models.CharField("airport", max_length = 100)
    international = models.BooleanField()
    google_id = models.CharField(max_length = 100)
    latitude = models.FloatField()
    longitude = models.FloatField()
