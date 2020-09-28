from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Language(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Book(models.Model):
    language = models.ForeignKey(
        'Language', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=454)
    author = models.CharField(max_length=454)
    publication_year = models.IntegerField(validators=[MinValueValidator(
        1000), MaxValueValidator(2020)], null=True, blank=True)
    book_description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
