from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm
from django.contrib.auth.decorators import login_required

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, "core/students/student_list.html", {"students": students})

# Detail view
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "core/students/student_detail.html", {"student": student})

# Create new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)

            # also create a linked User (username = roll_no)
            user = User.objects.create_user(
                username=form.cleaned_data["roll_no"],
                password="default123"
            )
            student.user = user
            student.save()
            form.save_m2m()  # save many-to-many (if any)
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "core/students/student_form.html", {"form": form})

# Update student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "core/students/student_form.html", {"form": form})

# Delete student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":  # confirm before delete
        # also delete linked User
        student.user.delete()
        student.delete()
        return redirect("student_list")
    return render(request, "core/students/student_confirm_delete.html", {"student": student})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "core/courses/course_list.html", {"courses": courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk)
    return render(request, "core/courses/course_detail.html", {"course": course})

def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "core/courses/course_form.html", {"form": form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "core/courses/course_form.html", {"form": form})

# Delete course
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request, "core/courses/course_confirm_delete.html", {"course": course})

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, "core/enrollments/enrollment_list.html", {"enrollments": enrollments})

def enrollment_detail(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    return render(request, "core/enrollments/enrollment_detail.html", {"enrollment": enrollment})

def enrollment_create(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
    else:
        form = EnrollmentForm()
    return render(request, "core/enrollments/enrollment_form.html", {"form": form})

def enrollment_update(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, "core/enrollment_form.html", {"form": form})

def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        enrollment.delete()
        return redirect("enrollment_list")
    return render(request, "core/enrollments/enrollment_confirm_delete.html", {"enrollment": enrollment})

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")