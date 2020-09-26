from django.db import models
from products.models import Book
from profiles.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),

)


class Review(models.Model):
    book = models.ForeignKey(Book, null=False, blank=False,
                             on_delete=models.CASCADE, related_name='reviews')
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(5)], null=False, blank=False, choices=RATING_CHOICES)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    review_text = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.rating} star review on order {self.book.title}'
