from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'basesite/base.html') #IMPORTANT NOTE - 'base.html' is
    #automatically found, as django takes all templates from (project)/(app)/templates
    #and considers them the same thing. may make things difficult if we have multiple apps

    # Also for dynamically rendered pages pass a dictionary into render, and
    # this will be used in Jinja templating

def search(request):
    sample = {'cars': [
    {'name': 'Toyota', 'type': 'Sedan', 'speed': 'Slow'},
    {'name': 'Ferarri', 'type': 'Racecar', 'speed': 'Fast'}
    ]
    }
    # note that each car in the cars list cannot be named. no dictionary of named dictionaries
    # also, 'cars' must refer to a list/array, not a dict

    return render(request, 'basesite/search.html', sample)