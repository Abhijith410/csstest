from django.shortcuts import render

# Create your views here.
def fun1(request):
    return render (request,"media.html",)

def fun2(request):
    return render (request, "messages.html",)

def fun3(request):
    return render (request, "profile.html",)        
