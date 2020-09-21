from django.shortcuts import get_object_or_404
from products.models import Book
from plans.models import Plan


def bag_contents(request):
    bag_items = []
    price_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, value in bag.items():
        print(value)
        plan = None
        book = None

        if value['type'] == 'book':
            book = get_object_or_404(Book, pk=item_id)
            price_total += value['quantity'] * book.price
        else:
            plan = get_object_or_404(Plan, pk=item_id)
            price_total += value['quantity'] * plan.price

        product_count += value['quantity']
        bag_items.append({
            'item_id': item_id,
            'quantity': value['quantity'],
            'book': book,
            'plan': plan,
        })

    context = {
        'bag_items': bag_items,
        'price_total': price_total,
        'product_count': product_count,
    }

    return context
