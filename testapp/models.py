from django.db import models

# Create your models here.
class Movie(models.Model):
    release_date = models.DateField()
    movie_name = models.CharField(max_length=40)
    hero = models.CharField(max_length=20)
    heroine = models.CharField(max_length=20)
    rating = models.IntegerField()