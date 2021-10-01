from django.shortcuts import render, redirect, reverse
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
        'stripe_publick_key': 'pk_test_51JfnSWHjOAJdLtL9sve284ntDkhaEsWnqn48ZtLZSGzqlV8Ia2joE8FYiErRSIAgoawCcz1nK9ZkOU788AlJYi1Q00ngCaZkGr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
