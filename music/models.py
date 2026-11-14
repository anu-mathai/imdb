from django.db import models
from film.models import Movie

# Create your models here.
class Song(models.Model):

    title=models.CharField(max_length=200)

    singer=models.CharField(max_length=200)

    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

    track_no=models.PositiveIntegerField()

    duration=models.CharField()

    def __str__(self):

        return self.title