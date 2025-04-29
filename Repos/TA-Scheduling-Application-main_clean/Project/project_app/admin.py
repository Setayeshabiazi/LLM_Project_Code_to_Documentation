from django.contrib import admin
from project_app.models import User, Course, Section
                            
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)