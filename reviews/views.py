from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from products.models import Book
from profiles.models import UserProfile

from .forms import ReviewForm


# Create your views here.
@login_required
def write_review(request, book_id):
    """A view to allow a user to create a review"""

    book = get_object_or_404(Book, pk=book_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            title = form.cleaned_data['title']
            review_text = form.cleaned_data['review_text']

            review = Review(
                book=book, user_profile=user,
                rating=rating, title=title, review_text=review_text)
            review.save()
            messages.success(
                request, 'Your review was successfully posted.')

            return redirect('book_detail', book_id=book.id)

        else:
            messages.error(request, 'There was an error while submitting your review. \
                Your title or review text might be too long.')

            context = {
                'form': form,
                'book': book,
                'user': user,
                'on_write_review_page': True,
            }

            template = 'reviews/write_review.html'

            return render(request, template, context)

    else:
        form = ReviewForm()

        context = {
            'form': form,
            'book': book,
            'user': user,
            'on_write_review_page': True,
        }

        template = 'reviews/write_review.html'

        return render(request, template, context)


def calculate_average_rating(book_id):
    """ Calculate average review rating per book """
    book = get_object_or_404(Book, pk=book_id)
    all_reviews = Review.objects.all()
    reviews = all_reviews.filter(book=book)
    average_rating = reviews.aggregate(Avg('rating'))
    return average_rating


def delete_review(request, review_id):
    """ Delete a review, currently
    only available on profile page for the user, who created the review """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Your review was deleted!')
    return redirect(reverse("profile"))
