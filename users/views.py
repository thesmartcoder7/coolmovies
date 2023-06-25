from stat import UF_OPAQUE
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


def signup(request):
    """
    View function for user signup.

    If the request method is POST, it processes the signup form data.
    If the form is valid, it creates a new user account and redirects to the login page.
    If the form is invalid, it renders the signup page with the form containing validation errors.

    If the request method is GET, it renders the signup page with an empty signup form.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The response containing the rendered template.

    """
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Thank you, {username}. Your account has been successfully created! Login to continue...")
            return redirect('users_login')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserSignupForm()
        return render(request, 'users/signup.html', {'form': form})


@login_required
def update(request):
    """
    View function for updating user profile.

    If the request method is POST, it processes the update form data.
    If both the user form and profile form are valid, it saves the updated information and redirects to the home page.

    If the request method is GET, it renders the update page with the user form and profile form.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The response containing the rendered template.

    """
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
