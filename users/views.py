from stat import UF_OPAQUE
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('movies_home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/update.html', context)