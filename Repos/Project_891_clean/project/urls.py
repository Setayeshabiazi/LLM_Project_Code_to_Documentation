   
from django.contrib import admin
from django.urls import path

from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

from project_app import views


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('profile/update_profile/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('profile/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('courses/', views.ViewCourses.as_view(), name='view_courses'),
    path('courses/create/', views.CreateCourse.as_view(), name='create_course'),
    path('courses/<int:course_id>/', views.ViewCourse.as_view(), name='view_course'),
    path('courses/<int:course_id>/edit/', views.EditCourse.as_view(), name='edit_course'),
    path('courses/<int:course_id>/delete/', views.DeleteCourse.as_view(), name='delete_course'),
                                                                        
                                                                        
    path('courses/<int:course_id>/sections/create/', views.CreateSection.as_view(), name='create_section'),
    path('courses/<int:course_id>/sections/<int:section_id>/edit', views.EditSection.as_view() , name='edit_section'),
    path('courses/<int:course_id>/sections/<int:section_id>/delete/', views.DeleteSection.as_view(), name='delete_section'),
                                                                                                  
                                                                                                  
    path('users/', views.ViewUsers.as_view(), name='view_users'),
    path('users/create/', views.CreateUser.as_view(), name='create_user'),
    path('users/<int:user_id>/', views.ViewUser.as_view(), name='view_user'),
    path('users/<int:user_id>/edit/', views.EditUser.as_view(), name='edit_user'),
    path('users/<int:user_id>/delete/', views.DeleteUser.as_view(), name='delete_user'),
                                                                                     
                                                                                             
                                                                                                       
                                                                                                                         
]
