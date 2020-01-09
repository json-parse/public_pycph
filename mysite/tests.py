from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.utils import timezone
from news.models import Article
from events.models import Event
from jobs.models import Job
from mysite.views import home


class HomeTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "password"
        )
        self.event = Event.objects.create(
            author=self.user,
            title="test",
            date=timezone.now(),
            location="place"
        )
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
        self.article = Article.objects.create(
            author=self.user,
            title="test",
            text="text test"
        )

    def test_home(self):
        request = self.factory.get('/some-fake/url')
        response = home(request)
        self.assertEqual(response.status_code, 200)
