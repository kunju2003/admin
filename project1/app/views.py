from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def user_form_dis(request):
    data=user_form()
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            roll=form.cleaned_data['roll']
            name=form.cleaned_data['name']
            mark=form.cleaned_data['mark']
            data1=student.objects.create(roll=roll,name=name,mark=mark)
            data1.save()
    return render(request,'user_std.html',{'data':data})