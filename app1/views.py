from .models import Lesson, Teacher, Student
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse


def TeacherView(request):
    post = Teacher.objects.all()
    return render(request, 'teacher.html', {"post": post})


class LessonView(TemplateView):
    template_name = 'Lesson.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers_id = kwargs['teachers_id']
        post = get_object_or_404(Teacher, id=teachers_id)
        posts = Lesson.objects.filter(teacher_id=post)
        context['post'] = post
        context['posts'] = posts
        return context


class StudentView(TemplateView):
    template_name = 'Student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lessons = kwargs['lessons']
        post = get_object_or_404(Lesson, name=lessons)
        posts = Student.objects.filter(lesson__name=lessons)
        context['post'] = post
        context['posts'] = posts
        return context

