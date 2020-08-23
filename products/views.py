from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

def all_books(request):
    """ A view for all books, searching and filtering"""

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)


def book_detail(request, book_id):
    """ A view for individual book details"""

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'products/book_detail.html', context)
