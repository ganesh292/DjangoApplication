# from django.os import path
import os
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http    import HttpResponse
from wsgiref.util import FileWrapper
from feedback.models import ScoreOneStimulus,VideoUrl
from feedback.views import updateScore
from user import views as user_views
from django.template import loader

# urls = [
#       "{% static 'video/video1.mp4' %}",
#       "{% static 'video/video2.mp4' %}",
#       "{% static 'video/video3.mp4' %}"',

#       ]
# urls = [ 'video/video1.mp4', 'video/video2.mp4', 'video/video3.mp4',

      # ]


video_lists = ['0001','0003']


# Create your views here.
def home(request):
    return render(request,'videoplay/home.html')
def fetchVideo(video_id_list):
#To fetch video url from database corresponding to each video id
	vid_url_list= []
	for item in video_id_list:
		print(item)
		vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
	return vid_url_list
# class PlayView(TemplateView):
#       template_name = 'videoplay/play.html'

#       def get(self, request):
#             # query=request.GET.get('score')#this variable holds the value of score
#             # message="The score is {}".format(query)
#             # context={'message':message,}
#             return render(request, self.template_name)#,context)
#       def post(self,request):
#             return render(request, self.template_name)


def play(request):
      #getting scores
      query=request.GET.get('score')
      message="The score is {}".format(query)
      context={'message':message,}
      return render(request, 'videoplay/play.html', context)

def download(request):
      #urls=fetchVideo(video_lists)
      #context1={}
      #context1['urls'] = ','.join([str(i) for i in urls])
      return render(request,'videoplay/download.html')#,context1)



