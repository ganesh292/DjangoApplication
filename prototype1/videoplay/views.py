# from django.os import path
from django.shortcuts import render
from django.http    import HttpResponse
# Create your views here.


news =['video1','video2','video3']



# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def videos(request):
    return render(request,'videoplay/play.html')
