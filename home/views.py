from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return the index page"""
    template = 'home/index.html'
    context = {
        'non_product_page': True,
    }
    return render(request, template, context)
