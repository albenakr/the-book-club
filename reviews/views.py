from django.shortcuts import render


# Create your views here.
def reviews(request):
    """A view to return the index page"""
    return render(request, 'reviews/reviews.html')