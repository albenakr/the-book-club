from django.shortcuts import (
    render, get_object_or_404)
from django.db.models import Q
from .models import Book, Genre, Language
from reviews.models import Review
from reviews.views import calculate_average_rating


def is_valid_queryparam(param):
    """ Validates data coming from filter options """
    return param != '' and param is not None


def all_books(request):
    """ A view to display all books, as well as searching and filtering"""
    """ Code inspired by JustDjango - details in README """
    books = Book.objects.all().order_by('-pk')
    genres = Genre.objects.all()
    languages = Language.objects.all()
    genre = request.GET.get('genre')
    language = request.GET.get('language')
    search_query = request.GET.get('q')
    filters = request.GET.get('filters')

    if is_valid_queryparam(search_query):
        books = books.filter(
            Q(title__icontains=search_query)
            | Q(book_description__icontains=search_query)
            | Q(author__icontains=search_query)
        ).distinct()

    if is_valid_queryparam(genre) and genre != 'Genres':
        books = books.filter(genre__name=genre)

    if is_valid_queryparam(language) and language != 'Languages':
        books = books.filter(language__name=language)

    if is_valid_queryparam(filters) and filters != 'Filter':
        if filters == 'price_asc':
            books = books.order_by('price')
        elif filters == 'price_desc':
            books = books.order_by('-price')
        elif filters == 'title_asc':
            books = books.order_by('title')
        elif filters == 'title_desc':
            books = books.order_by('-title')
        elif filters == 'author_asc':
            books = books.order_by('author')
        elif filters == 'author_desc':
            books = books.order_by('-author')

    context = {
        'books': books,
        'genres': genres,
        'languages': languages,
        'search_term': search_query,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view for overview of book details"""

    book = get_object_or_404(Book, pk=book_id)
    all_reviews = Review.objects.all()
    reviews = all_reviews.filter(book=book).order_by('-date')
    average_rating = calculate_average_rating(book_id=book.id)

    context = {
        'book': book,
        'reviews': reviews,
        'average_rating': average_rating['rating__avg'],
    }

    return render(request, 'products/book_detail.html', context)
