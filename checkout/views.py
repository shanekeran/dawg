from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JRDqDE8ngvsjJ2yGlqd24Tf8Overmrv9V5MbA76HF3vVm10DSudPvBfqn9UzV1eAyw7xQwt7fEZoD7MieWIvjwZ00WmwAodjK',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)

