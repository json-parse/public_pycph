from django.conf import settings
from django.db import models
from django.utils import timezone


class Event(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50)
    address_line_1 = models.CharField(blank=True, max_length=50)
    address_line_2 = models.CharField(blank=True, max_length=50)
    postcode = models.CharField(blank=True, max_length=4)
    link = models.URLField(blank=True, max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
