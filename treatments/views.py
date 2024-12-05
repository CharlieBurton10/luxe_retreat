from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Treatment

# Create your views here.

def all_treatments(request):
    """ A view to show all treatments, including sorting and search queries """

    treatments = Treatment.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('treatments'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            treatments = treatments.filter(queries)

    context = {
        'treatments': treatments,
        'search_term': query,
    }

    return render(request, 'treatments/treatments.html', context)