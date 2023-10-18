from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginForm, name='login'),
    
    # Dashboard URLs
    path('student/dashboard/', student_dashboard_view, name='student_dashboard'),
    path('faculty/dashboard/', faculty_dashboard_view, name='faculty_dashboard'),
    path('sponsor/dashboard/', sponsor_dashboard_view, name='sponsor_dashboard'),
]
