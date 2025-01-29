from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Treatment, Category
from .forms import TreatmentForm


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


@login_required
def add_treatment(request):
    """ Add a treatment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only managers can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save()
            messages.success(request, 'Successfully added Treatment!')
            return redirect(reverse('treatments'))
        else:
            messages.error(request, 'Failed to add treatment. Please ensure the form is valid.')
    else:
        form = TreatmentForm()

    template = 'treatments/add_treatment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_treatment(request, treatment_id):
    """ Edit a treatments already available """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only managers can do that.')
        return redirect(reverse('home'))

    treatment = get_object_or_404(Treatment, pk=treatment_id)
    if request.method == 'POST':
        form = TreatmentForm(request.POST, instance=treatment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Treatment!')
            return redirect(reverse('treatments'))
        else:
            messages.error(request, 'Failed to update Treatment. Please ensure the form is valid.')
    else:
        form = TreatmentForm(instance=treatment)
        messages.info(request, f'You are editing {treatment.name}')

    template = 'treatments/edit_treatment.html'
    context = {
        'form': form,
        'treatment': treatment,
    }

    return render(request, template, context)


@login_required
def delete_treatment(request, treatment_id):
    """ Delete a treatment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only managers can do that.')
        return redirect(reverse('home'))
    treatment = get_object_or_404(Treatment, pk=treatment_id)
    treatment.delete()
    messages.success(request, 'Treatment deleted!')
    return redirect(reverse('treatments'))
