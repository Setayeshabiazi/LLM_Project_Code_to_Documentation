from django.test import TestCase
from project_app.models import Course


class CoursesAcceptanceTestSuite(TestCase):
    def setUp(self):
                                           
        Course.objects.create(subject='COURSE1', number='101', name='Course 1')
        Course.objects.create(subject='COURSE2', number='201', name='Course 2')
        Course.objects.create(subject='COURSE3', number='301', name='Course 3')

    def test_get_course_by_subject_and_number(self):
                                                    
        course = Course.objects.get(subject='COURSE1', number='101')

                                                                 
        self.assertEqual(course.subject, 'COURSE1')
        self.assertEqual(course.number, '101')
        self.assertEqual(course.name, 'Course 1')

    def test_get_all_courses(self):
                                                
        courses = Course.objects.all()

                                                                           
        self.assertEqual(courses.count(), 3)

                                                                          
        self.assertEqual(courses[0].subject, 'COURSE1')
        self.assertEqual(courses[0].number, '101')
        self.assertEqual(courses[1].subject, 'COURSE2')
        self.assertEqual(courses[1].number, '201')
        self.assertEqual(courses[2].subject, 'COURSE3')
        self.assertEqual(courses[2].number, '301')
