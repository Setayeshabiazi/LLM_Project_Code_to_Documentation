from django.test import TestCase

from project_app.models import Role

from classes.ta_class import TAClass
from classes.course_class import CourseClass
from classes.section_class import SectionClass


class TAUnitTestSuite(TestCase):
    def setUp(self):
        self.course = CourseClass(name='Test', subject='TEST', number='001')
        self.course.save_details()
        self.course = self.course.get_model_instance()

        self.section = SectionClass(number='001', course=self.course)
        self.section.save_details()
        self.section = self.section.get_model_instance()

        self.ta_class = TAClass(username='ta', email='ta@uwm.edu', first_name='Test',
                                last_name='TA', courses=[self.course])
        self.ta_class.save_details()

        self.section.tas.add(self.ta_class.get_model_instance())

    def test_init_default(self):
        ta_class = TAClass(username='ta', email='ta@uwm.edu', first_name='Test',
                           last_name='TA', courses=[self.course])

        self.assertEqual(ta_class.username, 'ta')
        self.assertEqual(ta_class.email, 'ta@uwm.edu')
        self.assertEqual(ta_class.first_name, 'Test')
        self.assertEqual(ta_class.last_name, 'TA')
        self.assertEqual(ta_class.role, Role.TA)
        self.assertEqual(ta_class.phone_number, None)
        self.assertEqual(ta_class.home_address, None)
        self.assertEqual(ta_class.courses, [self.course])
        self.assertEqual(ta_class.sent_notifications, [])
        self.assertEqual(ta_class.received_notifications, [])

    def test_get_instance_default(self):
        ta_class = TAClass.get_instance(self.ta_class.get_model_instance())

        self.assertTrue(isinstance(ta_class, TAClass))

        self.assertEqual(ta_class.username, self.ta_class.username)
        self.assertEqual(ta_class.email, self.ta_class.email)
        self.assertEqual(ta_class.first_name, self.ta_class.first_name)
        self.assertEqual(ta_class.last_name, self.ta_class.last_name)
        self.assertEqual(ta_class.role, self.ta_class.role)
        self.assertEqual(ta_class.phone_number, self.ta_class.phone_number)
        self.assertEqual(ta_class.home_address, self.ta_class.home_address)
        self.assertEqual(ta_class.courses, self.ta_class.courses)
        self.assertEqual(ta_class.sent_notifications, self.ta_class.sent_notifications)
        self.assertEqual(ta_class.received_notifications, self.ta_class.received_notifications)

    def test_get_sections_default(self):
        self.assertEqual(list(self.ta_class.get_sections()), [self.section])

    def test_has_section_true(self):
        self.assertTrue(self.ta_class.has_section(self.section))

    def test_has_section_false(self):
        section_2 = SectionClass(number='002', course=self.course)
        section_2.save_details()

        self.assertFalse(self.ta_class.has_section(section_2))