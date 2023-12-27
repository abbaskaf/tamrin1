from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ['first_name']


class Lesson(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["name"]


class Student(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    lesson = models.ManyToManyField(Lesson, related_name='students')

    def __str__(self):
        return f"{self.name}-{self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["name"]
