from django.shortcuts import render
from .models import Membership


def all_memberships(request):
    """ A view to show all memberships, including sorting and search queries """

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships/memberships.html', context)
