from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def login(request):
    return render(request, 'users/login.html')


def signup(request):
    if request.method == 'POST':
        print('\n\n the code gets inside post check \n\n')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('\n\n the code gets inside the if valid function \n\n')
            username = form.cleaned_data.get('username')
            # form.save()
            messages.success(request, f"Thank you, {username}. Your accout has been successfuly created! Login to continue...")
            return redirect('users_login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})