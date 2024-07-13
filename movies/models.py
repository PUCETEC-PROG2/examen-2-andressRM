from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.
