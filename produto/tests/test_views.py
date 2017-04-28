from django.test import TestCase,Client
from  django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class ProdutoIndexViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_superuser(username='tropical',email='maique.rosa@gmail.com',password='troca123')
        self.client = Client()
        self.client.login(username='tropical',password='troca123')
        self.url = reverse('produto:index')

    def tearDown(self):
        pass

    def test_status_code_200(self):
        response = self.client.get(self.url)
        print(response)
        self.assertEqual(response.status_code,200);


    def test_esta_usando_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,"produto/index.html")
