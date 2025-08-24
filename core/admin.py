from django.contrib import admin
from .models import Student, Course, Enrollment
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "roll_no")
    search_fields = ("user__username", "roll_no")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "date_enrolled")
    list_filter = ("date_enrolled",)
