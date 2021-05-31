from django.shortcuts import render,redirect
from django.http import HttpResponse
from clgresults.models import *
from django.contrib import messages


# Create your views here.

def result(request):
    results = Result.objects.all()
    return render(request,'result.html',{'results':results})

def search(request):
    return render(request,'search.html')

def studentres(request):
    if request.method =="POST":
        name = request.POST['name']
        semester = request.POST['semester']
        results = Result.objects.all()
    for result in results:
        if name == result.name and semester == result.semester:
            return render(request, 'studentres.html',
                          {'name': name, 'Rollno': result.RollNo, 'Semester': semester, 'SPI': result.SPI,
                           'CPI': result.CPI})
        elif name != result.name and semester != result.semester:
            messages.info(request, 'Invalid Credentials, Please Enter Your Details again')
            return redirect('/search/')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        query = request.POST['query']
        k = Contact(name=name, email=email, phno=phno, query=query)
        k.save()

    return render(request, 'contact.html')