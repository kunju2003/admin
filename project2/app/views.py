from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def model_form_dis(request):
    data=model_form()
    if request.method=='POST':
        form=model_form(request.POST)
        form.save()
        return redirect(model_form_dis)
    return render(request,'model_form.html',{'data':data})