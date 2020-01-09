from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from news.models import Article
from news.views import article_list, article_detail


class ArticleTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "password"
        )
        self.article = Article.objects.create(
            author=self.user,
            title="test",
            text="text test"
        )

    # Model tests
    def test_str(self):
        self.assertEquals(str(self.article), self.article.title)

    def test_publish(self):
        self.article.publish()
        self.assertTrue(self.article.published_date)

    # View tests
    def test_article_list(self):
        request = self.factory.get('/some-fake/url')
        response = article_list(request)
        self.assertEqual(response.status_code, 200)

    def test_article_detail(self):
        request = self.factory.get('/some-fake/url')
        response = article_detail(request, pk=self.article.pk)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        # print(vars(Article.objects.first()))
