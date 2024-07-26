from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages as message

def home(request):
    # Check to see if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            message.success(request, 'Error logging in. Please try again')
            return redirect('home')

    else:
        return render(request, 'home.html',{})



def logout_user(request):

    logout(request)
    message.success(request, 'You have successfully logged out')
    return redirect('home')
