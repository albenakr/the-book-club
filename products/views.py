from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Genre, Language


def all_books(request):
    """ A view for all books, searching and filtering"""

    books = Book.objects.all()
    query = None
    genres = None
    languages = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            
            if 'direction' in request.GET:
                 direction = request.GET['direction']
                 if direction == 'desc':
                     sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)


        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            books = books.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'language' in request.GET:
            languages = request.GET['language'].split(',')
            books = books.filter(language__name__in=languages)
            languages = Language.objects.filter(name__in=languages)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search keywords")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(book_description__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
        'current_languages': languages,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view for individual book details"""

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
