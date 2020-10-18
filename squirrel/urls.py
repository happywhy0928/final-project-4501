from django.urls import path

from . import views

app_name = 'squirrel'

urlpatterns = [
        path('sightings/', views.index, name ='index'),
        path('map/', views.map, name = 'map'),
        path('sightings/add/', views.create_new, name = 'create new sighting'),
        path('sightings/stats/', views.stats, name = 'stats'),
        path('sightings/<unique_id>/', views.update, name='update'),
        ]
