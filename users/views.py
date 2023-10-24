from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        net_id = request.POST['email']
        register_number = request.POST['register_number']
        phone_number = request.POST['phone_number']
        status = request.POST['status']
        club = request.POST['club']
        password = request.POST['password'] 
        password2 = request.POST['password2'] 

        if password != password2:
            return render(request, "users/register.html", {
                "message": "Passwords must match."
            })
        # Create the student instance and save it to the database
        user = CustomUser.objects.create_user(
            username=username, email=net_id, register_number=register_number, 
            phone_number=phone_number, password=password, club=club, status=status
        )
        user.save()
        login(request, user)
        return redirect('index')  # Replace with the actual URL
    else:
        return render(request, 'users/register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        # Create the student instance and save it to the database
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'users/login.html')
