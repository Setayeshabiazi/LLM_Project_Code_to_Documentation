from django.test import TestCase
from project_app.models import User


class UserAcceptanceTest(TestCase):
    def test_create_user(self):
                           
        username = 'testuser'
        email = 'testuser@example.com'
        password = 'testpassword'
        role = 1                                            

        user = User(username=username, email=email, password=password, role=role)
        user.save()

                                             
        created_user = User.objects.get(username=username)

                                                              
        self.assertEqual(created_user.username, username)
        self.assertEqual(created_user.email, email)
        self.assertEqual(created_user.role, role)

    def test_update_user(self):
                           
        username = 'testuser'
        email = 'testuser@example.com'
        password = 'testpassword'
        role = 1                                            

        user = User(username=username, email=email, password=password, role=role)
        user.save()

                                             
        existing_user = User.objects.get(username=username)

                                                      
        new_email = 'updated_email@example.com'
        existing_user.email = new_email
        existing_user.save()

                                                   
        updated_user = User.objects.get(username=username)

                                                        
        self.assertEqual(updated_user.email, new_email)
