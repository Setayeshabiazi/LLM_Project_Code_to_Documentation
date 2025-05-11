from django.test import TestCase
from project_app.models import Course


class CreateCourseAcceptanceTest(TestCase):
    def test_create_course(self):
                                   
        subject = 'COURSE1'
        number = '101'
        name = 'Course 1'

                           
        course = Course(subject=subject, number=number, name=name)
        course.save()

                                                       
        created_course = Course.objects.get(subject=subject, number=number)

                                                                
        self.assertEqual(created_course.subject, subject)
        self.assertEqual(created_course.number, number)
        self.assertEqual(created_course.name, name)
