from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():#form validation
            form.save()# to save user info to your admin page
            username=form.cleaned_data.get('username')# retrieves user name
            messages.success(request, f'Account created for {username}!. You can now Log in')#alert message for user creation
            return redirect('login')# redirects you to 'name=some_name' page after submission
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})
