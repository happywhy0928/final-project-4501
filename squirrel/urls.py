from django.urls import path

from . import views

app_name = 'squirrel'

urlpatterns = [
        path('', views.index, name ='index'),
        path('<unique-squirrel-id>/', views.detail, name='detail'),
        ]
