from django.db import models
from products.models import Book

# Create your models here.


class PlanDuration(models.Model):
    duration_months = models.IntegerField()

    def __str__(self):
        return str(self.duration_months) + " months"


class Plan(models.Model):
    name = models.CharField(max_length=454)
    books = models.ManyToManyField(Book)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    plan_duration = models.ForeignKey('PlanDuration', default='3', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

