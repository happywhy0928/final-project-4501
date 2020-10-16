from django.shortcuts import render
from squirrel.models import Squirrel
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


import random

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,

            }
    return render(request, 'squirrel/index.html', context)

def detail(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)

    context = {
            'Squirrel':squirrel,
    }

    return render(request, 'squirrel/detail.html', context)
