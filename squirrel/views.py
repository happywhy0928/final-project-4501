from django.shortcuts import render
from squirrel.models import Squirrel
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .forms import CreateNewSighting
from .forms import UpdateSighting
import random

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,

            }
    return render(request, 'squirrel/index.html', context)

def update(request, unique_id):
    squirrel = get_object_or_404(Squirrel,unique_id = unique_id)
    form = UpdateSighting(request.POST or None, instance=squirrel)
    context = {
            'UpdateSighting':form,
    }
    if form.is_valid():
        squirrel = form.save(commit=False)
        squirrel.save()
        return redirect('/sightings/')
    else:
        context = {
            'form':form,
        }
        return render(request, 'squirrel/update.html', context)


def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel/map.html', context)


def create_new(request):
    if request.method == 'POST':
        form = CreateNewSighting(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = CreateNewSighting()
        context = {
                'form':form,
            }
        return render(request, 'squirrel/create.html', context)

def stats(request):
     Number_of_Juvenile = Squirrel.objects.filter(age = 'Juvenile').count()
     Morning = Squirrel.objects.filter(shift = 'AM').count()
     BlackFur = Squirrel.objects.filter(furColor = "black").count()
     Eatings = Squirrel.objects.filter(eating = True).count()
     Runnings = Squirrel.objects.filter(running = True).count()
     print(Number_of_Juvenile)
     context = {
            "Number_of_Juvenile":Number_of_Juvenile,            
            "Morning":Morning,
            "BlackFur":BlackFur,
            "Eatings":Eatings,
            "Runnings":Runnings,
            }
     return render(request,'squirrel/stat.html', context)

