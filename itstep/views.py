from django.shortcuts import render
from .models import Teacher, Course, Student


def index(request):
    return render(request, "itstep/index.html")


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "itstep/teachers.html", {"teachers": teachers})


def courses_list(request):
    courses = Course.objects.all()
    return render(request, "itstep/courses.html", {"courses": courses})


def students_list(request):
    students = Student.objects.all()
    return render(request, "itstep/students.html", {"students": students})

