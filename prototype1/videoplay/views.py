from django.shortcuts import render
from django.http    import HttpResponse
# Create your views here.


context = {
    'id1' : 'video/video1.mov',
    'id2' : 'video/video2.mov'
    

}



# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def videos(request):
    return render(request,'videoplay/play.html')
