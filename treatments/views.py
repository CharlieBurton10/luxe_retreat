from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Treatment, Category
from .forms import TreatmentForm

# Create your views here.

def all_treatments(request):
    """ A view to show all treatments, including sorting and search queries """

    treatments = Treatment.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            treatments = treatments.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'current_categories': categories,
    }

    return render(request, 'treatments/treatments.html', context)

def add_treatment(request):
    """ Add a treatment to the store """
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Treatment!')
            return redirect(reverse('add_treatment'))
        else:
            messages.error(request, 'Failed to add treatment. Please ensure the form is valid.')
    else:    
        form = TreatmentForm()

    template = 'treatments/add_treatment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)