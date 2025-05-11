from project_app.models import Role

from classes.user_class import UserClass


class TAClass(UserClass):
    def __init__(self, username, email, first_name, last_name, phone_number=None, home_address=None, courses=[],
                 received_notifications=[]):
        super().__init__(username, email, first_name, last_name, Role.TA,
                         phone_number, home_address, courses, [], received_notifications)

    @classmethod
    def get_instance(cls, ta):
        return cls(
            ta.username, 
            ta.email, 
            ta.first_name, 
            ta.last_name, 
            ta.phone_number, 
            ta.home_address, 
            list(ta.courses.all())
        )

    def validate(self):
        super().validate()

        if self.role is not Role.TA:
            raise ValidationError('Role is not TA.')

    def get_sections(self):
        ta = self.get_model_instance()
        return ta.section_set.all()

    def has_section(self, section):
        ta = self.get_model_instance()
        return ta.section_set.filter(course=section.course, number=section.number).exists()
