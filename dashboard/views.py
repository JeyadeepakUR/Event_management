from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event

@login_required
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
        return render(request, 'dashboard/faculty_home.html')
    elif user.status == 'spo':
        return render(request, 'dashboard/sponsor_home.html')
    else:
        return HttpResponse(f"Unauthorized, {user.status}")

def about(request):
    return render(request, 'dashboard/about.html')

@login_required
def events(request):
    events = Event.objects.all().order_by('start_datetime')
    return render(request, 'dashboard/events.html', {
        "events": events
    })

@login_required
def new_event(request):
    if request.user.is_organiser:
        if request.method == 'POST':
            event_name = request.POST['event_name']
            event_location = request.POST['event_location']
            event_type = request.POST['event_type']
            event_description = request.POST['event_description']
            start_datetime = request.POST['start_datetime']
            end_datetime = request.POST['end_datetime']
            organizer_name = request.POST['organizer_name']
            organizer_club = request.POST['organizer_club']
            organizer_phone = request.POST['organizer_phone']
            organizer_email = request.POST['organizer_email']
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
                organizer_name=organizer_name,
                organizer_club=organizer_club,
                organizer_phone=organizer_phone,
                organizer_email=organizer_email
            )
            event.save()

            return redirect('events')  # Redirect to a success page or event list

        return render(request, 'dashboard/new_event.html')
    else:
        return HttpResponse("Unauthorized")
    
@login_required
def elevate(request):
    return render(request, 'dashboard/elevation.html')