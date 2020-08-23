from django.shortcuts import render
from .models import Book

# Create your views here.

def all_books(request):
    """ A view for all books, searching and filtering"""

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)
