from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    template = 'index.html'

    return render(request, template)
