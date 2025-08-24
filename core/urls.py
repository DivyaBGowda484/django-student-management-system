from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list, name = 'student_list'),
    path("students/add/", views.student_create, name="student_create"),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path("students/<int:pk>/edit/", views.student_update, name="student_update"),
    path("students/<int:pk>/delete/", views.student_delete, name="student_delete"),

    path("courses/", views.course_list, name="course_list"),
    path("courses/add/", views.course_create, name="course_create"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/<int:pk>/edit/", views.course_update, name="course_update"),
    path("courses/<int:pk>/delete/", views.course_delete, name="course_delete"),

    path("enrollments/", views.enrollment_list, name="enrollment_list"),
    path("enrollments/<int:pk>/", views.enrollment_detail, name="enrollment_detail"),
    path("enrollments/create/", views.enrollment_create, name="enrollment_create"),
    path("enrollments/<int:pk>/update/", views.enrollment_update, name="enrollment_update"),
    path("enrollments/<int:pk>/delete/", views.enrollment_delete, name="enrollment_delete"),
]