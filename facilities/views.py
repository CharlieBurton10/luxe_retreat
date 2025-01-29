from django.shortcuts import render


def facilities(request):
    """ A view to return the facilities page """

    return render(request, 'facilities/facilities.html')
