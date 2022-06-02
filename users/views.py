from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Thank you, {username}. Your accout has been successfuly created! Login to continue...")
            return redirect('users_login')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserSignupForm()
        return render(request, 'users/signup.html', {'form': form})