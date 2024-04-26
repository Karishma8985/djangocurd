
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .models import *


def Student_view(request):
    return render(request,'student.html',{})

def Student_register(request):
    name=request.POST['uname']
    age=request.POST['age']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    address=request.POST['address']
    gender=request.POST['gender']
    pics=request.FILES['pics']
    student=Student(name=name,age=age,email=email,password=password,phone=phone,address=address,gender=gender,pics=pics)
    student.save()
    
    messages.info(request, "data register successfully.", fail_silently=True)
    return redirect('/show_student')
    
    
def show_student(request):
    student=Student.objects.all()
    return render(request,'show_student.html',{'student':student})

def edit_student(request,id):
    student=Student.objects.get(id=id)
    return render(request,'edit_student.html',{'student':student})
    
def update_student(request,id):
    student=Student.objects.get(pk=id)
    student.name=request.POST['uname']
    student.age=request.POST['age']
    student.email=request.POST['email']
    student.password=request.POST['password']
    student.phone=request.POST['phone']
    student.address=request.POST['address']
    student.gender=request.POST['gender']
    student.pics=request.FILES['pics']
    
    student.save()
    student=Student.objects.all()
    return redirect('/show_student',student)

def delete_student(request,id):
    sdel=Student.objects.get(pk=id)
    sdel.delete()
    student=Student.objects.all()
    return redirect('/show_student',student)

def slogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Student.objects.filter(email=email,password=password).exists():
            return redirect('/student_view')
        else:   
            messages.info(request, "invalid email or password.", fail_silently=True)
            return redirect('/slogin')
    return render(request,'slogin.html',{})
    