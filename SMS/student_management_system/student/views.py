from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def display_student_view(request):
    students = Student.objects.all()

    context = {
        'student' : students,
    }

    return render(request, 'display-student.html' , context)

def create_student_view(request):
    context = dict()

    context = {
        'operation':'Create Student',
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        marks = request.POST.get('marks')
        address = request.POST.get('address')
        course = request.POST.get('course')

        if name and roll_no and marks and address and course:
            Student.objects.create(name=name, roll_no=roll_no, marks=marks, address=address,course=course)
            return redirect('display')
        else:
             context['errors'] = 'All fields are required.'

    return render(request, 'student-form.html', context)

def update_student_view(request,student_id):
    context = dict()

    try:
        student = Student.objects.get(id=student_id)
        context['student'] = student
    except Student.DoesNotExist:
        context['errors'] = '404: Student not found'

    context['operation'] = 'Update Student'

    if request.method == 'POST':
        name = request.POST.get('name',)
        roll_no = request.POST.get('roll_no')
        marks = request.POST.get('marks')
        address = request.POST.get('address')
        course = request.POST.get('course')

        student.name=name
        student.roll_no=roll_no
        student.marks=marks
        student.address=address
        student.course=course

        student.save()
        return redirect('display')
    
    return render(request, 'student-form.html', context)

def delete_student_view(request, student_id):
    context=dict()

    try:
        student = Student.objects.get(id=student_id)
        context['student'] = student
    except Student.DoesNotExist:
        context['errors'] = '404: Student not found'

    if request.method == 'POST':
        student.delete()
        return redirect('display')

    return render(request,'delete-student.html',context)
