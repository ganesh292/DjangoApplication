# # from django.os import path
# import os
# from django.views.generic import TemplateView
# from django.conf import settings
# from django.shortcuts import render
# from django.http    import HttpResponse
# from wsgiref.util import FileWrapper
# from feedback.models import ScoreOneStimulus,VideoUrl
# from feedback.views import updateScore
# from user import views as user_views
# from django.template import loader

# # urls = [
# #       "{% static 'video/video1.mp4' %}",
# #       "{% static 'video/video2.mp4' %}",
# #       "{% static 'video/video3.mp4' %}"',

# #       ]
# # urls = [ 'video/video1.mp4', 'video/video2.mp4', 'video/video3.mp4',

#       # ]


# video_lists = ['0001','0003']


# # Create your views here.
# def home(request):
#     return render(request,'videoplay/home.html')
# def fetchVideo(video_id_list):
# #To fetch video url from database corresponding to each video id
# 	vid_url_list= []
# 	for item in video_id_list:
# 		print(item)
# 		vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
# 	return vid_url_list
# # class PlayView(TemplateView):
# #       template_name = 'videoplay/play.html'

# #       def get(self, request):
# #             # query=request.GET.get('score')#this variable holds the value of score
# #             # message="The score is {}".format(query)
# #             # context={'message':message,}
# #             return render(request, self.template_name)#,context)
# #       def post(self,request):
# #             return render(request, self.template_name)


# def play(request):
#       #getting scores
#       #query=request.user;
#       query=request.GET.get('score')
#       message="The score is {}".format(query)
#       context={'message':message,}
#       return render(request, 'videoplay/play.html', context)

# def download(request):
#       #urls=fetchVideo(video_lists)
#       #context1={}
#       #context1['urls'] = ','.join([str(i) for i in urls])
#       return render(request,'videoplay/download.html')#,context1)


# from django.os import path
import os
import json
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from feedback.models import ScoreOneStimulus, VideoUrl
#from feedback.views import updateScore
from user import views as user_views
from django.template import loader
import re
from django.shortcuts import redirect

# urls = [
#       "{% static 'video/video1.mp4' %}",
#       "{% static 'video/video2.mp4' %}",
#       "{% static 'video/video3.mp4' %}"',

#       ]
# urls = [ 'video/video1.mp4', 'video/video2.mp4', 'video/video3.mp4',
# ]
username = ''
stat_url = ["{% static url%}"]

# ]

#video_lists = ['0000001', '0000002']
# video_lists = ['0001','0003']
#Jatin's Backend code
video_lists = ['0000001', '0000002']


def checkUserExists(username):
	#To check if newuser or existing user?
	obj = ScoreOneStimulus.userScore.filter(user_name=username)
	# print(obj)
	if(len(obj) == 0):
		return False
	else:
		return True
# def NewEntry(username,video_id_list):
# #To insert initial data into the table
# 	for item in video_id_list:
# 		obj=ScoreOneStimulus(user_name=username,session_id=1,vid_id=item)
# 		obj.save()


def NewEntry(username, sid=1):
	#To insert initial data into the table

      for item in video_lists:
            print("Inside NewEntry Function and gonna add ", item, "\n")
            obj = ScoreOneStimulus(
            	user_name=username, session_id=sid, vid_id=item)
            obj.save()
      return video_lists


def checkSession(username):
	#To check if its new session or old session
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).filter(score__isnull=True)
	if(len(obj) == 0):
		return ('newsession', 'Dummy')
	else:
		vid_sublist = []
		for item in obj:
			vid_sublist.append(item.vid_id)
		return ('oldsession', vid_sublist)
	# print(len(obj))
	# return


def incSessionId(username):
	#To increment sessionid after fetching last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return (obj.session_id + 1)

# def fetchVideo(video_id_list):
# #To fetch video url from database corresponding to each video id
# 	vid_url_list= []
# 	for item in video_id_list:
# 		print(item)
# 		vid_url_list.append(Video_Url.objects.get(vid_id=item).vid_url)
# 	return vid_url_list


def findSessionId(username):
	#To find last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	# print(obj.session_id)
	return obj.session_id


def updateScore(username, sid, vid, scr):
	# To update score in the database table
	obj = ScoreOneStimulus.userScore.get(
		user_name=username, session_id=sid, vid_id=vid)
	# print(obj.score)
	obj.score = scr
	obj.save()
	return


def backendlogic(username, scr=50):
      # print(checkUserExists(username))
      if checkUserExists(username) == False:
            # print("calling New entry")
            NewEntry(username)
            return video_lists
      else:
            if(checkSession(username)[0] == 'oldsession'):
                  # print('oldsession')
                  return checkSession(username)[1]
            else:
                  sid = incSessionId(username)
                  return NewEntry(username, sid)


def update_urllookup():
      data = open('static/video_list.txt', 'r',).read()
      rows = re.split('\n', data)  # splits along new line
      for index, row in enumerate(rows):
            cells = row.split(' ')
            obj = VideoUrl(vid_id=cells[0], vid_url='http://' + cells[1])
            obj.save()
            # print(cells)
      return
#update_urllookup()


def fetchVideo(video_id_list):
      #To fetch video url from database corresponding to each video id
      vid_url_list = []
      print("I am inside Fetch Video Function\n")
      for item in video_id_list:
            print(item)
            vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
      return vid_url_list


def download(request):
      print(request.user)
      print("I am inside download and gonna call backened logic")
      video_lists1 = backendlogic(request.user, 98)
      print(video_lists1)
      urls = fetchVideo(video_lists1)
      print(urls)
      context1 = {}
      context1['urls'] = ','.join([str(i) for i in urls])
      return render(request, 'videoplay/download.html/', context1)

query=0
query1=""
# Create your views here.
def home(request):
    return render(request, 'videoplay/home.html')
# def fetchVideo(video_id_list):
# #To fetch video url from database corresponding to each video id
# 	vid_url_list= []
# 	for item in video_id_list:
# 		print(item)
# 		vid_url_list.append(VideoUrl.urlobj.get(vid_id=item).vid_url)
# 	return vid_url_list
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
      # query=request.user;
      # url = request.POST.get('score',"")
      # print(url)
      query =request.GET.get('score')
      #print(query)
      # query1=request.GET.get('videoID')
      # # # query2 = request.GET.get('videoID')
      # # query2 = '0000002'
      # # if(query == None or query2 == None):
      # #       print("query is", query)
      # #       pass
      # # else:
      # #       updateScore(request.user,findSessionId(request.user),query2,query)
      # #       print('Bingo!')
      # #       print("score.....", query)
      # #       print(" I am in Play Function .......vid_id....", query2)
      # #       print("Sid", findSessionId(request.user))
      # message = "Thank You for watching! {}".format(query)
      # context = {'message': message,}
      # return render(request, 'videoplay/play.html',context)
      # if request.method == 'POST':
      #       JSONdata = request.POST['data']
      #       dict = simplejson.JSONDecoder().decode(JSONdata)
      #       query=dict['score']
      #       message = "Thank You for watching! {}".format(query)
      #       context = {'message': message, }
      #       # doSomething with pieFact here...
      #       return render(request, 'videoplay/temp.html', context)
      return render(request, 'videoplay/play.html')

# def download(request):
#       #urls=fetchVideo(video_lists)
#       #context1={}
#       #context1['urls'] = ','.join([str(i) for i in urls])
#       return render(request,'videoplay/download.html')#,context1)

def temp(request):
      #query = request.GET.get('score')
      #query1=request.GET.get('videoID')
      if request.method == 'POST':
            query = json.loads(request.POST['score'])
            print(query)
            message = "Thank You for watching! {}".format(query)
            context = {'message': message, }
            # doSomething with pieFact here...
            return render(request, 'videoplay/temp.html', context)
      return render(request, 'videoplay/temp.html')
