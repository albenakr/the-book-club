from django.shortcuts import render
from .models import Review


# Create your views here.
def reviews(request):
    """A view to return the index page"""
    reviews = Review.objects.all()

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)
