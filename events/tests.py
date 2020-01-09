from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.utils import timezone
from events.models import Event
from events.views import event_list, event_detail


class EventTestCase(TestCase):
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

    # Model tests
    def test_str(self):
        self.assertEquals(str(self.event), self.event.title)

    def test_publish(self):
        self.event.publish()
        self.assertTrue(self.event.published_date)

    # View tests
    def test_event_list(self):
        request = self.factory.get('/some-fake/url')
        response = event_list(request)
        self.assertEqual(response.status_code, 200)

    def test_event_detail(self):
        request = self.factory.get('/some-fake/url')
        response = event_detail(request, pk=self.event.pk)
        self.assertEqual(response.status_code, 200)
