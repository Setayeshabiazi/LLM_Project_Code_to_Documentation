from django.test import TestCase

from classes.ta_class import TAClass
from project_app.models import Course, Section, User, Role

from classes.instructor_class import InstructorClass
from classes.course_class import CourseClass
from classes.section_class import SectionClass
from classes.notification_class import NotificationClass


class InstructorUnitTestSuite(TestCase):
    def setUp(self):
        self.instructor_class = InstructorClass(username='instructor', email='instructor@uwm.edu',
                               first_name='Test', last_name='Instructor')
        self.instructor_class.save_details()

        self.course = CourseClass(name='Test', subject='Test', number='Test')
        self.course.save_details()
        self.course = self.course.get_model_instance()

        self.ta = TAClass(username='TA', email='ta@uwm.edu', first_name='Test', last_name=' TA')
        self.ta.save_details()
        self.ta.add_course(self.course)
        self.ta = self.ta.get_model_instance()

        self.section = SectionClass(number='1', course=self.course, ta=self.ta)
        self.section.save_details()
        self.section = self.section.get_model_instance()

    def test_init_default(self):
        instructor_class = InstructorClass(username='instructor', email='instructor@uwm.edu',
                          first_name='Test', last_name='Instructor', courses=[self.course])

        self.assertEqual(instructor_class.username, 'instructor')
        self.assertEqual(instructor_class.email, 'instructor@uwm.edu')
        self.assertEqual(instructor_class.first_name, 'Test')
        self.assertEqual(instructor_class.last_name, 'Instructor')
        self.assertEqual(instructor_class.role, Role.INSTRUCTOR)
        self.assertEqual(instructor_class.phone_number, None)
        self.assertEqual(instructor_class.home_address, None)
        self.assertEqual(instructor_class.courses, [self.course])
        self.assertEqual(instructor_class.sent_notifications, [])
        self.assertEqual(instructor_class.received_notifications, [])
    
    def test_get_instance_default(self):
        instructor_class = InstructorClass.get_instance(self.instructor_class.get_model_instance())

        self.assertTrue(isinstance(instructor_class, InstructorClass))

        self.assertEqual(instructor_class.username, self.instructor_class.username)
        self.assertEqual(instructor_class.email, self.instructor_class.email)
        self.assertEqual(instructor_class.first_name, self.instructor_class.first_name)
        self.assertEqual(instructor_class.last_name, self.instructor_class.last_name)
        self.assertEqual(instructor_class.role, self.instructor_class.role)
        self.assertEqual(instructor_class.courses, self.instructor_class.courses)
        self.assertEqual(instructor_class.sent_notifications, self.instructor_class.sent_notifications)
        self.assertEqual(instructor_class.received_notifications, self.instructor_class.received_notifications)

    def test_validate_default(self):
        pass

    def test_assign_ta_section_default(self):
        self.instructor_class.assign_ta_section(self.ta, self.section)

                                                 
        self.assertIn(self.section.course, self.ta.courses.all())
    
    def test_assign_ta_section_ta_does_not_exist(self):
        invalid_ta = TAClass('invalid', 'invalid@uwm.edu', 'Invalid', 'TA')

        with self.assertRaises(TypeError, msg='assign_ta_section does not raise TypeError for non-existant TA'):
            self.instructor_class.assign_ta_section(invalid_ta, self.section)

    def test_assign_ta_section_section_does_not_exist(self):
        invalid_section = SectionClass('ABC', None)

        with self.assertRaises(AttributeError, msg='assign_ta_section does not raise AttributeError for non-existant section'):
            self.instructor_class.assign_ta_section(self.ta, invalid_section)

    def test_get_sent_notifications_default(self):
        self.assertEqual(self.instructor_class.get_sent_notifications(), [])

    def test_send_notifications_default(self):
        notifications = self.instructor_class.send_notifications(self.course, 'Subject', 'Message')
        notification = notifications[0]

        instructor = self.instructor_class.get_model_instance()

        self.assertIn(notification, instructor.sent_notifications.all())
        self.assertNotIn(notification, instructor.received_notifications.all())

        self.assertNotIn(notification, self.ta.sent_notifications.all())
        self.assertIn(notification, self.ta.received_notifications.all())

    def test_send_notifications_course_does_not_exist(self):
        invalid_course = CourseClass('', '')

        with self.assertRaises(Course.DoesNotExist, msg='send_notifications does not raise Course.DoesNotExist for non-existant course'):
            self.instructor_class.send_notifications(invalid_course, 'Subject', 'Message')
