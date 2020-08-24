from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book


def all_books(request):
    """ A view for all books, searching and filtering"""

    books = Book.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search keywords")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(book_description__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view for individual book details"""

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
