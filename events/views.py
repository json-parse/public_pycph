from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from jobs.models import Job

def event_list(request):
    events = Event.objects.filter(published_date__lte=timezone.now()).filter(date__gte=timezone.now()).order_by('date')
    jobs = Job.objects.filter(approved_job=True).filter(last_application_date__gte=timezone.now()).order_by('-created_date')
    return render(request, 'events/event_list.html', {'events': events, 'jobs' : jobs})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    other_events = Event.objects.exclude(pk=pk).filter(published_date__lte=timezone.now()).filter(date__gte=timezone.now()).order_by('date')[:4]
    return render(request, 'events/event_detail.html', {'event': event, 'other_events' : other_events})