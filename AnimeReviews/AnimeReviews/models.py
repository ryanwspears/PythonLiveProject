from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Anime(models.Model):
    animeName = models.CharField(max_length=100)
    numOfEpisodes = models.IntegerField()
    studioName = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(max_length=1500)

    objects = models.Manager()

    def __str__(self):
        return self.animeName
