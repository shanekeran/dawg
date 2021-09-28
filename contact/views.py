from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Contact
from .forms import ContactUs


def contact_form(request):

    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid:
            contact = form.save()
            messages.success(request, 'Dawg has received your message!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Unable to send your message. Please review your submission and try again.')
    else:
        form = ContactUs()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'non_product_page': True
    }

    return render(request, template, context)
