from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article
from events.models import Event
from jobs.models import Job


def article_list(request):
    articles = Article.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    events = Event.objects.filter(
        published_date__lte=timezone.now()).filter(
            date__gte=timezone.now()).order_by('date')
    jobs = Job.objects.filter(approved_job=True).filter(
        last_application_date__gte=timezone.now()).order_by('-created_date')
    return render(
        request, 'news/article_list.html',
        {'articles': articles, 'events': events, 'jobs': jobs}
    )


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    other_articles = Article.objects.exclude(pk=pk).filter(
        published_date__lte=timezone.now()).order_by('-published_date')[:4]
    return render(
        request, 'news/article_detail.html',
        {'article': article, 'other_articles': other_articles}
    )
