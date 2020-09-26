from django.shortcuts import render, get_object_or_404
from .models import Review
from products.models import Book
from profiles.models import UserProfile

from .forms import ReviewForm


# Create your views here.
def reviews(request):
    """A view to return the index page"""
    reviews = Review.objects.all()

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


def write_review(request, book_id):

    book = get_object_or_404(Book, pk=book_id)
    print(book)
    user = get_object_or_404(UserProfile, user=request.user.id)
    print(user)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            rating = form.cleaned_data['rating']
            print(rating)
            title = form.cleaned_data['title']
            print(title)
            review_text = form.cleaned_data['review_text']
            print(review_text)

            review = Review(book=book, user=user, rating=rating, title=title,
                            review_text=review_text)
            review.save()

            context = {
                'review': review,
            }
            return render(request, 'reviews/write_review.html', context)

    else:
        form = ReviewForm()


        context = {
            'form': form,
        }

        template = 'reviews/write_review.html'


        return render(request, template, context)
