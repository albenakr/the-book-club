from django.db import models
from products.models import Book

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=454)
    books = models.ManyToManyField(Book)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
