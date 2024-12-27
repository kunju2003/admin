from django.shortcuts import render,redirect
from .models import *
# from .forms import *

# Create your views here.
def upload_file(request):
    if request.method=='POST':
        filename=request.FILES['file']
        des=request.POST['des']
        data=files.objects.create(file=filename,description=des)
        data.save()
        return redirect(upload_file)
    return render(request,'media.html')