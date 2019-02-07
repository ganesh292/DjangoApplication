# from django.os import path
import os
import getpass
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http    import HttpResponse
from wsgiref.util import FileWrapper
from feedback.models import ScoreOneStimulus
from feedback.views import updateScore

# urls = [
#       "{% static 'video/video1.mp4' %}",
#       "{% static 'video/video2.mp4' %}",
#       "{% static 'video/video3.mp4' %}"',

#       ]
urls = [ 'video/video1.mp4', 'video/video2.mp4', 'video/video3.mp4',

      ]
username = ''
stat_url = ["{% static url%}"]

context1 = {'static':stat_url ,'urls': urls,'username':username}

# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')

class PlayView(TemplateView):
      template_name = 'videoplay/play.html'

      def get(self, request):
            posts=ScoreOneStimulus.userScore.all()
            return render(request, self.template_name)
      def post(self,request):
            searchWord = request.POST.get('username_problem')
            updateScore(searchWord,1,"video1.mp4",100)
            return render(request, self.template_name)

def download(request):
    print(request.user.username)
    return render(request,'videoplay/download.html',context1)



