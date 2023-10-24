from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/new/', views.new_event, name='new_event'),
    path('events/<int:eid>', views.single_event, name='event'),
    path('events/', views.events, name='events'),
    path('elevate/', views.elevate, name='elevate'),
    path('logout/', views.logout_view, name="logout"),
    path('org_req/<int:uid>/', views.handle_orgreq, name='org_req'),
]