from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import CustomPlanForm
from products.models import Book, Genre, Language
from .models import Plan
import random


# Create your views here.


def plans(request):
    """A view to return the index page"""
    return render(request, 'plans/plans.html')


def custom_plans(request):
    """A view to return a custom plans page"""

    books = Book.objects.all()
    genres = Genre.objects.all()
    languages = Language.objects.all()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomPlanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = str(form.cleaned_data['name'])
            print(name)
            genres = list(form.cleaned_data['genres'])
            print(genres)
            languages = list(form.cleaned_data['languages'])
            print(languages)
            plan_duration = int(form.cleaned_data['plan_duration'])
            print(plan_duration)

            # Filter books by genre and language
            books = books.filter(genre__name__in=genres).filter(
                language__name__in=languages)
            print(books)

            if len(books) == 0:
                messages.info(request, 'No results found for your search. Please try again')
                form = CustomPlanForm()
                context = {
                    'form': form,
                }
                return render(request, 'plans/custom_plan_form.html', context)

            if len(books) < plan_duration:
                plan_duration = len(books)
                messages.info(request, f'{plan_duration} books found for your search. Your plan has been adjusted to {plan_duration} months')

            # Shuffle Books and limit the result to the number of month in plan_duration
            # https://pynative.com/python-random-module/
            # plan duration acts as limit
            shuffled_books = list(random.sample(list(books), plan_duration))
            print(shuffled_books)

            # create a fallback in case there are not enough books in the categories they want

            # generate price by number of months in plan_duration multiplied by EUR 10
            price = plan_duration * 10
            print(price)

            # create a new instance of Plan, by assigning name, books, price
            custom_plan = Plan(
                name=name, price=price)
            custom_plan.save()
            custom_plan.books.set(shuffled_books)

            books_from_custom_plan = custom_plan.books.all()
            print(books_from_custom_plan)

            context = {
                'custom_plan': custom_plan,
                'books_from_custom_plan': books_from_custom_plan,
            }

            # redirect to a new URL, giving customer an overview of the books in their plan and allowing them to either add it to their bag or restart the survey
            return render(request, 'plans/custom_plan_details.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomPlanForm()

    context = {
        'form': form,
    }

    return render(request, 'plans/custom_plan_form.html', context)


def surprise_plans(request):
    """A view to return the surprise plans page"""

    return render(request, 'plans/surprise_plan.html')
