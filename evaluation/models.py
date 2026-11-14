from django.db import models

# Create your models here.
from film.models import Movie
from django.contrib.auth.models import User

class Review(models.Model):

    message=models.CharField(max_length=200)

    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    rating=models.CharField(max_length=100)

    class Meta:

        unique_together=("movie","owner")

    def __str__(self):
     return f"Review for {self.movie.title} by {self.owner.username}"   