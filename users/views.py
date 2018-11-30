from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #to save user in database with all secure background we nee only->
            form.save()
            #cleaned_data is a dictionary with data from 'form'
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}!')
            return redirect('blog-home') #blog-home is name of url in urls.py
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form' : form })

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
