from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/new/', views.new_event, name='new_event'),
    path('events/', views.events, name='events'),
    path('elevate/', views.elevate, name='elevate'),
]