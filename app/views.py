from django.shortcuts import render
from .models import aman
from .forms import mahajan
# Create your views here.
def sukritan(request):
    forms=mahajan()
    if request.method =="POST":
        n1=request.POST.get('name')
        n2=request.POST.get('rollno')
        user=aman(name=n1,rollno=n2)
        user.save()
        candidate=aman.objects.all()
       
        return render(request,"index.html",{"forms":forms,'candidate':candidate})
    else:
        candidate=aman.objects.all()
        return render(request,"index.html",{"forms":forms,'candidate':candidate})

def candidate(request,pk):
    user=aman.objects.get(pk=pk)
    return render (request,"candidate.html",{"candidate":user})
