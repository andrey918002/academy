from django.contrib import admin
from .models import Teacher, Course, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "start", "end")
    list_filter = ("teacher", "start")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    list_filter = ("courses",)
    search_fields = ("first_name", "last_name", "email")

