from django.shortcuts import render
from .models import Treatment

# Create your views here.

def all_treatments(request):
    """ A view to show all treatments, including sorting and search queries """

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)