from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeacherView),
    path('lesson/<slug:teachers_id>', views.LessonView.as_view(), name='lesson_list'),
    path('student/<slug:lessons>', views.StudentView.as_view(), name='lesson')
]
