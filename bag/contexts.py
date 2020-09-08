from django.shortcuts import get_object_or_404
from products.models import Book


def bag_contents(request):
    bag_items = []
    price_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        book = get_object_or_404(Book, pk=item_id)
        price_total += quantity * book.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })

    context = {
        'bag_items': bag_items,
        'price_total': price_total,
        'product_count': product_count,
    }

    return context
