from django import forms
from .models import Student, Course, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["roll_no", "courses"]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "code"]

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["student", "course"]