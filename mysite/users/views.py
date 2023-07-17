from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # For user authentication
from django.contrib import messages # To display any messages(for eg while signup)
from .forms import RegisterForm # Form we created using UserCreationForm to add email field as well

# Create your views here.

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # No email field
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been successfully created.')
            return redirect('login')
    else:    
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form}) #This means that {'form':form} is passed to the template user/register.html

@login_required #Decorator used to restrict access to this view until user is logged in
def profilepage(request):
    return render(request, 'users/profile.html') # Used to send model to html template