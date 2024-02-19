from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
from django.shortcuts import redirect
from student.models import Student,User
import json 


def home(request):
    return render(request,'student/home.html')
def contact(request):
    return render(request,'student/contact.html')
def about(request):
    return render(request,'student/about.html')


def student(request):
    students=Student.objects.all()
    context={}
    context['students']=students
    return render(request,'student/home.html',context)

def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return redirect('student')

def signup(request):
    if request.method=='GET':
        return render(request,'student/signup.html')

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['psw']
        name=request.POST['name']
        val=User.objects.filter(email=email)
        if val:
         context = {
                'error_message': "Invalid email please try again"
            }
         return render(request,'student/signup.html',context)
           
        User.objects.create(email=email,password=password,name=name)

        return redirect('student')
    
def signin(request) :
    if request.method == 'GET':
        
        return render(request,'student/login.html')
    
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['psw']
        val=User.objects.filter(email=email,password=password)
        if val:
            return redirect("student")
        else:
            context={'error_message':'Incorrect email or password'}
            return render(request,'student/login.html' ,context)
def create(request) :
    if request.method=='GET':
        return render(request,'student/create_student.html')
    if request.method=='POST':
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        age=request.POST['age']
        Student.objects.create(f_name=f_name,l_name=l_name,age=age)
        return redirect('student')

def update(request,id) :
    student=Student.objects.get(id=id)
    context={}
    context['students']=student 
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        student.f_name = fname
        student.l_name = lname
        student.age = age
        student.save()
        return redirect('student')
    return render(request,'student/update.html',context)
  
