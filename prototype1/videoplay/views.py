from os import path
from django.shortcuts import render
from django.http    import HttpResponse
# Create your views here.


# import glib
# downloads_dir = glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)

# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def videos(request):
    return render(request,'videoplay/play.html')
