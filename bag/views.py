from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Book
from plans.models import Plan

# Create your views here.


def view_bag(request):
    """A view that renders the bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of a specified product to the shopping bag"""

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        #updated_quantity += quantity 
        bag[item_id] = {'quantity': quantity + 1, 'type': 'book'}
        messages.success(request, f'Updated {book.title} quantity to {bag[item_id]["quantity"]}')
    else:
        bag[item_id] = {'quantity': quantity, 'type': 'book'}
        messages.success(request, f'{book.title} was added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def add_plan_to_bag(request, item_id):
    """ Add plan"""

    plan = get_object_or_404(Plan, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    bag[item_id] = {'quantity': quantity, 'type': 'plan'}
    messages.success(request, f'{plan.name} was added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of a specified product in the shopping bag"""

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id]['quantity'] = quantity
        messages.success(request, f'Updated {book.title} quantity to {bag[item_id]["quantity"]}')
    else:
        bag.pop[item_id]
        messages.success(request, f'{book.title} was removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """ Remove item from the shopping bag"""

    book = get_object_or_404(Book, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{book.title} was removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def remove_plan_from_bag(request, item_id):
    """ Remove item from the shopping bag"""

    plan = get_object_or_404(Plan, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{plan.name} was removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
