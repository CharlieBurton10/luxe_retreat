from django.shortcuts import render

# Create your views here.
def facilities(request):
    """ A view to return the facilities page """

    return render(request, 'facilities/facilities.html')
