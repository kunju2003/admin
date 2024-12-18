from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from . models import *

# Create your views here.
def register(request):
    departments=department.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        dep=request.POST['d']
        current_dep=department.objects.get(pk=dep)
        data=employee.objects.create(name=name,email=email,password=password,username=username,dname=current_dep)
        data.save()
    return render(request,'employee.html',{'deps':departments})
    

admname="adm123"
admpassword="adm@123"
def adminlog(request):
    if request.method=='POST':
       username=request.POST['name']
       password=request.POST['password']
       if username==admname and password==admpassword:
           print("logged in")
           request.session['adm']=admname
           return redirect(adminhome)
    return render(request,'adminlog.html')


def adminhome(request):
    emps=employee.objects.all()
    deps=department.objects.all()
    if request.method=='POST':
       dep=request.POST['d']
       deppk=department.objects.get(pk=dep)
       emps=employee.objects.filter(dname=deppk)
    # if 'adm' in request.session:
    #    user=User.objects.all()
    #     # user=User.objects.filter(username__startswith="n")
    #    print(user)
    return render(request,'adminhome.html',{'deps':deps,'emps':emps})
      
    # else:
    #    return redirect(adminlog)

