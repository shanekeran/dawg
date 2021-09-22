from django.shortcuts import render
from . models import Location


def list_locations(request):

    """
    Gets all Location objects from the database.
    """

    locations = Location.objects.all()
    context = {
        "locations": locations,
    }
    return render(request, "locations/locations.html", context)
