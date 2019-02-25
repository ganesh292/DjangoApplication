from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from feedback import views as entry_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():#form validation
            form.save()# to save user info to your admin page
            username=form.cleaned_data.get('username')# retrieves user name
            # entry_views.NewEntry(username)
            return redirect('login')# redirects you to 'name=some_name' page after submission
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})



