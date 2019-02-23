# from django.os import path
import os
import getpass
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http    import HttpResponse
from wsgiref.util import FileWrapper
from feedback.models import ScoreOneStimulus,VideoUrl
from feedback.views import *
from user import views as user_views
from django.template import loader

# urls = [
#       "{% static 'video/video1.mp4' %}",
#       "{% static 'video/video2.mp4' %}",
#       "{% static 'video/video3.mp4' %}"',

#       ]
# urls = [ 'video/video1.mp4', 'video/video2.mp4', 'video/video3.mp4',
# ]
username = ''
stat_url = ["{% static url%}"]

# context1 = {'static':stat_url ,'urls': urls,'username':username}
      # ]


video_lists = ['0001','0002','0003']


# Create your views here.
def home(request):
    
    return render(request,'videoplay/home.html')
def fetchVideo(video_id_list):
#To fetch video url from database corresponding to each video id
	vid_url_list= []
	for item in video_id_list:
		vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
	return vid_url_list
class PlayView(TemplateView):
      template_name = 'videoplay/play.html'

      def get(self, request):
            posts=ScoreOneStimulus.userScore.all()
            return render(request, self.template_name)
      def post(self,request):
            # searchWord = request.POST.get('username_problem')
            print(request.user.username)
            updateScore(request.user.username,1,"0001",100)
            return render(request, self.template_name)

class download(TemplateView):
      def get(self, request):
            status = checkUserExists(request.user.username)
            if status == 'newuser':
                 
                  NewEntry(request.user.username)
            urls=fetchVideo(video_lists)
            context1={}
            context1['urls'] = ','.join([str(i) for i in urls])
            return render(request,'videoplay/download.html',context1)



