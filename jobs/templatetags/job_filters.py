from django import template
from jobs.models import LOCATION_CHOICES, JOB_TYPE_CHOICES, SENIORITY_LEVEL_CHOICES

register = template.Library()


@register.filter
def location(value):
    location_choices_dict = dict(LOCATION_CHOICES)
    return location_choices_dict.get(value)


@register.filter
def jobtype(value):
    job_type_choices_dict = dict(JOB_TYPE_CHOICES)
    return job_type_choices_dict.get(value)


@register.filter
def seniority(value):
    seniority_choices_dict = dict(SENIORITY_LEVEL_CHOICES)
    return seniority_choices_dict.get(value)
