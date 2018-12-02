from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #to save user in database with all secure background we nee only->
            form.save()
            #cleaned_data is a dictionary with data from 'form'
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account was created successfully, now you are able to log in')
            return redirect('login') #blog-home is name of url in urls.py
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form' : form })

#login_required is a decorator, basicly it adds extra functionality to our function below it
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
