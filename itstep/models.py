from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courses")
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date_of_birth = models.DateField()
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

