from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Job
from .forms import JobForm
from events.models import Event
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


def job_list(request):
    approved_jobs = Job.objects.filter(approved_job=True).filter(
        last_application_date__gte=timezone.now()).order_by('-created_date')
    events = Event.objects.filter(published_date__lte=timezone.now()).filter(
        date__gte=timezone.now()).order_by('date')
    return render(
        request, 'jobs/job_list.html',
        {'approved_jobs': approved_jobs, 'events': events}
    )


def job_detail(request, pk):
    job = get_object_or_404(Job.objects.filter(approved_job=True), pk=pk)
    other_jobs = Job.objects.exclude(pk=pk).filter(approved_job=True).filter(
        last_application_date__gte=timezone.now()
        ).order_by('-created_date')[:4]
    return render(
        request, 'jobs/job_detail.html',
        {'job': job, 'other_jobs': other_jobs}
    )


def job_new(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_date = timezone.now()
            job.save()
            subject = 'New job offer'
            message = "Pls approve job offer {job.title} posted on {datetime.now().strftime('%a, %d %b %Y %H:%M')}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@pycph.com']
            send_mail(subject, message, email_from, recipient_list,)
            return redirect('job_draft', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'jobs/job_edit.html', {'form': form})


def job_draft(request, pk):
    job = get_object_or_404(Job.objects.filter(approved_job=False), pk=pk)
    return render(request, 'jobs/job_draft.html', {'job': job})
