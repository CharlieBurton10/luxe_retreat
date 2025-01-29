from django.conf import settings
from django.shortcuts import get_object_or_404
from treatments.models import Treatment


def bag_contents(request):

    bag_items = []
    total = 0
    treatment_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        treatment = get_object_or_404(Treatment, pk=item_id)
        total += quantity * treatment.price
        treatment_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'treatment': treatment,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'treatment_count': treatment_count,
    }

    return context
