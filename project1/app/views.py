from django.shortcuts import render
from .forms import *

# Create your views here.
def user_form_dis(requset):
    data=user_form()
    return render(requset,'user_std.html',{'data':data})