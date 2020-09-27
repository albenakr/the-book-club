from django.db import models
from products.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=454)
    books = models.ManyToManyField(Book)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    plan_duration = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(12)], null=True, blank=True)

    def __str__(self):
        return self.name
