from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LogoutViewTest(TestCase):
    def setUp(self):
                                  
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_logout_view(self):
                                                 
        response = self.client.get(reverse('logout'))

                                                                
        self.assertEqual(response.status_code, 302)

                                                         
        self.assertFalse(response.wsgi_request.user.is_authenticated)

                                                                                 
        self.assertRedirects(response, reverse('home'))
