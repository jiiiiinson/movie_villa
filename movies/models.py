from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.cname


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='img', blank=True)
    year = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    actors = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)], blank=True)

    # class Meta:
    #     unique_together = ('movie', 'user')

    def __str__(self):
        return f'Review by {self.user.username} for {self.movie}'
