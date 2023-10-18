from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import Loginform

def LoginForm(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.groups.filter(name='Student').exists():
                    login(request, user)
                    return redirect('student_dash')
                elif user.groups.filter(name='Faculty').exists():
                    login(request, user)
                    return redirect('faculty_dash')
    else:
        form = Loginform()
    return render(request, 'registration/Loginform.html', {'form': form})

def student_dashboard_view(request):
    return render(request, 'student_dashboard.html')

def faculty_dashboard_view(request):
    return render(request, 'faculty_dashboard.html')