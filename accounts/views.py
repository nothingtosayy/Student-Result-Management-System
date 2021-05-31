from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from clgresults.models import Result
# Create your views here.
def register(request):
    results = Result.objects.all()
    name_list = []
    for result in results:
        name_list.append(result.name)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if username in name_list:
            messages.info(request,"We found that you are a student, You don't have access to register. To view your Result navigate to search Page")
            return redirect('/')

        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
        return redirect('/')
    else:
        return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!.  Your Username/Password might be wrong')
            return redirect('/login/')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

