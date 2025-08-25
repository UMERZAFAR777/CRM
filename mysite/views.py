from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from student.models import Student

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')  
        password = request.POST.get('password')
        remember  = request.POST.get('remember')

        try:
            user_obj = User.objects.get(email = email)
            user = authenticate(request,username = user_obj.username ,password = password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login (request,user)
            if not remember:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(60 * 60 * 24 *30)    
            return redirect ('home')
        else:
            messages.error(request,"There was a error plz try again.........!")
            return redirect ('login')     
    return render (request,'login.html')       

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            messages.success (request,'Both password doesnt match..!')
            return redirect ('signup')
        
        if User.objects.filter(email = email).exists():
            messages.success (request,'Email is Already Taken.....!')
            return redirect ('signup')
        
        if User.objects.filter(username = username).exists():
            messages.success (request,'Username is Already Taken.....!')
            return redirect ('signup')
        
        user = User.objects.create_user(username= username , email= email , password= password)

        messages.success (request,"Your account is created successfully......!")
        return redirect ('login')
    

    return render (request,'signup.html')


def home(request):
    student = Student.objects.all()
    data = {
        'student':student
    }
    return render (request,'home.html',data)


def logout(request):
    auth_logout(request,)
    messages.success(request,'You have been logged out.....!')
    return redirect ('login')



def addstudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        eu = Student(name = name , city = city , email = email , phone = phone)

        eu.save()

        messages.success (request,'Student Record Added Successfully......!')\
        

        return redirect ('home')


    return render (request,'addstudent.html')


