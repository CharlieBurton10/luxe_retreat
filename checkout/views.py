from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.

def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request,
                        "There's nothing in your basket at the moment")
        return redirect(reverse('treatments'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QVDKcI8CkP3NIzzie68q36caHckUFjP1KPdosbY30d1PtFb8Aar3b7RrMqU28EUIqzZb2LGews71VTQHjQlvNAc004GZR6DU0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
