from django.shortcuts import render
from django.http    import HttpResponse
# Create your views here.



# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def videos(request):
    return render(request,'videoplay/play.html')
