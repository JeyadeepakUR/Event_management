from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.register, name='register'),
    path('login/', views.signin, name='login'),
]