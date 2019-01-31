# from django.os import path
import os
from django.conf import settings
from django.shortcuts import render
from django.http    import HttpResponse
from wsgiref.util import FileWrapper

# urls = [
#       "{% static 'video/video1.mp4' %}",
#       "{% static 'video/video2.mp4' %}",
#       "{% static 'video/video3.mp4' %}"',

#       ]
urls = [ 'video/video1.mp4', 'video/video2.mp4', 'video/video3.mp4',

      ]
stat_url = ["{% static url%}"]

context1 = {'static':stat_url ,'urls': urls}

# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def videos(request):
    return render(request,'videoplay/play.html')

def download(request):

    return render(request,'videoplay/download.html',context1)




  



