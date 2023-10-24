from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Event
from users.models import CustomUser

@login_required
def handle_orgreq(request, uid):
    if request.method == 'POST':
        user = CustomUser.objects.get(pk=uid)
        approval = request.POST.get('approval', None)

        if approval == 'Approve':
            user.org_req = 'appr'
            user.is_organizer = True
            user.save()
        elif approval == 'Deny':
            user.org_req = 'den'
            user.save()

    return redirect(reverse('index')) 

@login_required()
def index(request):
    user = request.user

    if user.status == 'stu': 
        display_events = Event.objects.all()[:6]
        highlight_events = Event.objects.filter(is_highlight=True).order_by('start_datetime')
        return render(request, 'dashboard/index.html', {
            "highlight_events": highlight_events,
            "display_events": display_events
        })
    elif user.status == 'fac': 
        students = CustomUser.objects.filter(status='stu')
        organizer_requests = CustomUser.objects.filter(org_req='pend')
        current_organizers = CustomUser.objects.filter(is_organizer=True)
        events = Event.objects.all()
        return render(request, 'dashboard/faculty_home.html', {
            'students': students,
            'organizer_requests': organizer_requests,
            'current_organizers': current_organizers,
            'events': events
        })
    elif user.status == 'spo':
        return render(request, 'dashboard/sponsor_home.html')
    else:
        return redirect('login')

def about(request):
    return render(request, 'dashboard/about.html')

@login_required
def events(request):
    events = Event.objects.all().order_by('start_datetime')
    return render(request, 'dashboard/events.html', {
        "events": events
    })

@login_required
def single_event(request, eid):
    try:
        event = Event.objects.get(pk=eid)
    except Exception as e:
        print("Error in getting the object", str(e))
        return HttpResponse(f'Error in getting the object + {str(e)}')
    
    current_datetime = timezone.now()
    upcoming_events = Event.objects.filter(start_datetime__gt=current_datetime).order_by('start_datetime')[:3]

    return render(request, "dashboard/single_event.html", {
        "event": event,
        "upcoming_events": upcoming_events
    })
        

@login_required
def new_event(request):
    if request.user.is_organizer:
        if request.method == 'POST':
            event_name = request.POST['event_name']
            event_location = request.POST['event_location']
            event_type = request.POST['event_type']
            event_description = request.POST['event_description']
            start_datetime = request.POST['start_datetime']
            end_datetime = request.POST['end_datetime']
            # organizer_name = request.POST['organizer_name']
            # organizer_club = request.POST['organizer_club']
            # organizer_phone = request.POST['organizer_phone']
            # organizer_email = request.POST['organizer_email']
            event_banner = request.FILES['event_banner']  
            entry_fee = request.POST['entry_fee']

            # Create a new Event instance and save it to the database
            event = Event(
                event_name=event_name,
                event_location=event_location,
                event_type=event_type,
                event_description=event_description,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                event_banner=event_banner,  
                entry_fee=entry_fee,
                organizer=request.user
                # organizer_name=organizer_name,
                # organizer_club=organizer_club,
                # organizer_phone=organizer_phone,
                # organizer_email=organizer_email
            )
            event.save()

            return redirect('events')  # Redirect to a success page or event list

        return render(request, 'dashboard/new_event.html')
    else:
        return HttpResponse("Unauthorized")
    
@login_required
def elevate(request):
    user = request.user
    if request.method == 'POST':
        user.org_req = 'pend'
        user.save()
        
        
    return render(request, 'dashboard/elevation.html', {
        "org_req": user.org_req
    })

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))