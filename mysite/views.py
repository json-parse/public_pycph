from django.shortcuts import render
from django.utils import timezone
from news.models import Article
from events.models import Event
from jobs.models import Job


def error_404_view(request, exception):
    return render(request, 'mysite/error_404.html')


def home(request):
    articles = Article.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')[:3]
    events = Event.objects.filter(published_date__lte=timezone.now()).filter(
        date__gte=timezone.now()).order_by('date')[:3]
    jobs = Job.objects.filter(approved_job=True).filter(
        last_application_date__gte=timezone.now()
        ).order_by('-created_date')[:3]
    return render(
        request, 'mysite/home.html',
        {'articles': articles, 'events': events, 'jobs': jobs}
    )
