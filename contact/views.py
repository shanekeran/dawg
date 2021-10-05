from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactUs


def contact_form(request):

    if request.method == 'POST':
        form = ContactUs(request.POST)
        # Submits the form if inputted information is valid
        if form.is_valid():
            form.save()
            # display success message
            messages.success(request, 'Dawg has received your message!')
            return redirect(reverse('home'))
        else:
            # If form isn't valid, display error message.
            messages.error(request,
                            'Error. Review your submission and try again.')
    else:
        form = ContactUs()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'non_product_page': True
    }

    return render(request, template, context)
