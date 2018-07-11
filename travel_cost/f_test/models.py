from django.db import models

# Create your models here.
class Countries_Cities(models.Model):
    country = models.CharField("country", max_length = 100)
    city = models.CharField("city", max_length = 100)
    country_rus = models.CharField("страна", max_length = 100)
    city_rus = models.CharField("город", max_length = 100)
    airport = models.CharField("airport", max_length = 100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Plan(models.Model):
     date = models.DateField("Дата", auto_now=True)  
     city = models.CharField("Город", max_length = 100)
     place = models.CharField("Место", max_length = 150)
     note = models.CharField("Заметка", max_length = 300) 
     link = models.CharField("Ссылка", max_length = 200)