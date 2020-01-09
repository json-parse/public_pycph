from django.db import models
from django.utils import timezone

LOCATION_CHOICES = (
    (1, "Copenhagen"),
    (2, "Frederiksberg"),
    (3, "Albertslund"),
    (4, "Ballerup"),
    (5, "Brøndby"),
    (6, "Furesø"),
    (7, "Gentofte"),
    (8, "Gladsaxe"),
    (9, "Glostrup"),
    (10, "Greve Strand"),
    (11, "Herlev"),
    (12, "Hvidovre"),
    (13, "Ishøj"),
    (14, "Lyngby-Taarbæk"),
    (15, "Rødovre"),
    (16, "Rudersdal"),
    (17, "Tårnby"),
    (18, "Vallensbæk"),
    (19, "Skåne"),
    (20, "Outside Greater Copenhagen")
)
JOB_TYPE_CHOICES = (
    (1, "Not specified"),
    (2, "Full-time"),
    (3, "Part-time"),
    (4, "Student job"),
    (5, "Internship")
)
SENIORITY_LEVEL_CHOICES = (
    (1, "Not specified"),
    (2, "Senior"),
    (3, "Mid level"),
    (4, "Junior"),
    (5, "Entry level")
)


class Job(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    contact = models.EmailField()
    company = models.CharField(max_length=100)
    location = models.IntegerField(choices=LOCATION_CHOICES, default=1)
    postcode = models.CharField(blank=True, max_length=4)
    job_type = models.IntegerField(choices=JOB_TYPE_CHOICES, default=1)
    seniority_level = models.IntegerField(
        choices=SENIORITY_LEVEL_CHOICES,
        default=1
    )
    last_application_date = models.DateField()
    apply_link = models.URLField(blank=True, max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    approved_job = models.BooleanField(default=False)

    def approve(self):
        self.approved_job = True
        self.save()

    def __str__(self):
        return self.title
