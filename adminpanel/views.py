from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout
from django.contrib import messages
from student.models import Student
# Create your views here.


def is_admin(user):
    return user.is_superuser



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username , password = password)

        if user is not None and user.is_superuser:
            auth_login(request,user)
            
            return redirect ("dashboard")
        
        else:
            messages.error(request,"There was a error plz try again or u r not a admin.......!")
            

    return render (request,'admin/admin_login.html')


@login_required(login_url="admin_login")
@user_passes_test(is_admin,login_url="admin_login")
def dashboard(request):
    student = Student.objects.all()
    data = {
        'student':student
    }
    return render (request,'admin/dashboard.html',data)



@login_required(login_url="admin_login")
def admin_logout(request):
    auth_logout(request)
    return redirect ('admin_login')


@login_required(login_url="admin_login")
def edit_student(request,id):
    student = Student.objects.get(id = id)
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        student.name = name if name else student.name
        student.city = city if city else student.city
        student.phone = phone if phone else student.phone
        student.email = email if email else student.email

        student.save()

        messages.success(request,'Edited Successfully.......!')

        return redirect ('dashboard')

    data ={
        'student':student
    }
    return render (request,'admin/edit_student.html',data)


@login_required(login_url="admin_login")
def delete_student(request,id):
    student = Student.objects.filter(id = id)

    student.delete()

    messages.success(request,"Student Deleted Successfully.....!")

    return redirect ('dashboard')







