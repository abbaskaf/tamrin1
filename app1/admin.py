from django.contrib import admin
from .models import Teacher, Lesson, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name",)
    list_filter = ("first_name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('teacher__first_name', 'teacher__last_name', 'name',)
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age',)
    list_filter = ('lesson',)
    search_fields = ('name',)
