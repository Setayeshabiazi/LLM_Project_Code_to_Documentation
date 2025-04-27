from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileViewTest(TestCase):
    def setUp(self):
                                  
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
                                                  
        response = self.client.get(reverse('profile'))

                                                          
        self.assertEqual(response.status_code, 200)
