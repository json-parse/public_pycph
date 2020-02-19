from django.test import TestCase, RequestFactory
from django.utils import timezone
from jobs.models import Job
from jobs.views import job_list, job_detail, job_draft, job_new

class JobTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.job = Job.objects.create(
            title="test",
            text="text test",
            contact="a@a.com",
            company="name",
            location=1,
            job_type=1,
            seniority_level=1,
            last_application_date=timezone.now()
        )

    # Model tests
    def test_str(self):
        self.assertEquals(str(self.job), self.job.title)

    def test_approve(self):
        self.job.approve()
        self.assertTrue(self.job.approved_job)

    # View tests
    def test_job_list(self):
        request = self.factory.get('/')
        response = job_list(request)
        self.assertEqual(response.status_code, 200)

    def test_job_draft(self):
        request = self.factory.get('/')
        response = job_draft(request, pk=self.job.pk)
        self.assertEqual(response.status_code, 200)

    def test_job_detail(self):
        Job.objects.update(
            id=self.job.id,
            approved_job=True
        )
        request = self.factory.get('/')
        response = job_detail(request, pk=self.job.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_job_new(self):
        request = self.factory.get('/')
        response = job_new(request)
        self.assertEqual(response.status_code, 200)
