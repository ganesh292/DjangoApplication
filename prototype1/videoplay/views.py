# from django.os import path
import os
from django.shortcuts import render
from django.http    import HttpResponse
from wsgiref.util import FileWrapper
from django.templatetags.static import static
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from zipfile import ZipFile

# Create your views here.


news =['video1','video2','video3']



# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def videos(request):
    return render(request,'videoplay/play.html')
def download(request):
    return render(request,'videoplay/download.html')

def filedownload(request):

    vid_list=[]
    in_memory = StringIO()
    zip = ZipFile(in_memory, "a")
    zip.writestr('static/video/video1.mp4',"content")

    response = HttpResponse(mimetype="application/zip")
    response["Content-Disposition"] = "attachment; filename=two_files.zip"
    
    in_memory.seek(0)    
    response.write(in_memory.read())
    
    return response

  



