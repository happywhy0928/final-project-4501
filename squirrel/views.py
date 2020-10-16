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

def detail(request, unique_id):
    squirrel = Squirrel.objects.filter(unique_id = unique_id)[0]

    context = {
            'squirrel':squirrel,
    }
    print(squirrel.date)
    print(squirrel.age)
    return render(request, 'squirrel/detail.html', context)
