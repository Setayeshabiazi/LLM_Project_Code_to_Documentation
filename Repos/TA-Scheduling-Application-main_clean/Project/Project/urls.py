   
from django.contrib import admin
from django.urls import path
from project_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('home/createCourse/', CreateCourse.as_view()),
    path('home/addSection/', AddSection.as_view()),
    path('home/createDeleteAccount/', CreateDeleteAccount.as_view()),
    path('home/accountEdit/', AccountEdit.as_view()),
    path('home/assignSection/', AssignSection.as_view()),
    path('home/assignCourse/', AssignCourse.as_view()),
    path('home/addSkills/', AddSkills.as_view()),
    path('home/viewSkills/', ViewSkills.as_view())
]
