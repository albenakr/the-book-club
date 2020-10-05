from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CustomPlanForm
from products.models import Book, Genre, Language
from .models import Plan
import random


def plans(request):
    """A view to return the index page"""
    return render(request, 'plans/plans.html')


def custom_plans(request):
    """A view to create a custom plan"""

    books = Book.objects.all()
    genres = Genre.objects.all()
    languages = Language.objects.all()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomPlanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = str(form.cleaned_data['name'])
            genres = list(form.cleaned_data['genres'])
            languages = list(form.cleaned_data['languages'])
            plan_duration = int(form.cleaned_data['plan_duration'])

            """Filter books by genre and language"""
            books = books.filter(genre__name__in=genres).filter(
                language__name__in=languages)

            """create a fallback in case there aren't enough books
            in the categories they want"""
            if len(books) == 0:
                messages.info(
                    request, 'No results found for your search. Please try again')
                form = CustomPlanForm()
                context = {
                    'form': form,
                }
                return render(request, 'plans/custom_plan_form.html', context)

            if len(books) < plan_duration:
                plan_duration = len(books)
                messages.info(
                    request, f'{plan_duration} books found for your search. Your plan has been adjusted to {plan_duration} months')

            """Shuffle Books and limit the result
            to the number of months in plan_duration"""
            shuffled_books = list(random.sample(list(books), plan_duration))

            # calculate price plan - each book in the plan cost a flat 10EUR
            price_per_book = 10
            price = plan_duration * price_per_book

            # create a new instance of Plan, by assigning name, books, price
            custom_plan = Plan(
                name=name, price=price, plan_duration=plan_duration)
            custom_plan.save()
            custom_plan.books.set(shuffled_books)

            books_from_custom_plan = custom_plan.books.all()

            # calculate how much they're saving from buying the plan
            overall_book_price = 0
            for book in books_from_custom_plan:
                book_price = book.price
                overall_book_price += book_price
            savings = overall_book_price - price

            context = {
                'custom_plan': custom_plan,
                'books_from_custom_plan': books_from_custom_plan,
                'savings': savings,
            }

            return render(request, 'plans/custom_plan_details.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomPlanForm()

    context = {
        'form': form,
    }

    return render(request, 'plans/custom_plan_form.html', context)


def view_custom_plan_details(request, plan_id):
    custom_plan = get_object_or_404(Plan, pk=plan_id)
    books_from_custom_plan = custom_plan.books.all()

    context = {
        'custom_plan': custom_plan,
        'books_from_custom_plan': books_from_custom_plan,
    }

    return render(request, 'plans/custom_plan_details_overview.html', context)
