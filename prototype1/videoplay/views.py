import os
import json
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from videoplay.models import ScoreOneStimulus, VideoUrl
from user import views as user_views
from django.template import loader
import re
from django.shortcuts import redirect
username = ''
stat_url = ["{% static url%}"]

#Jatin's Backend code
video_lists = ['0000001', '0000002']
# jatin's changes moving to master

def checkUserExists(username):
	#To check if newuser or existing user?
	obj = ScoreOneStimulus.userScore.filter(user_name=username)
	if(len(obj) == 0):
		return False
	else:
		return True


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


def incSessionId(username):
	#To increment sessionid after fetching last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return (obj.session_id + 1)


def findSessionId(username):
	#To find last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return obj.session_id


def updateScore(username, sid, vid, scr):
	# To update score in the database table
	obj = ScoreOneStimulus.userScore.get(
		user_name=username, session_id=sid, vid_id=vid)
	obj.score = scr
	obj.save()
	return


def backendlogic(username, scr=50):
      if checkUserExists(username) == False:
            NewEntry(username)
            return video_lists
      else:
            if(checkSession(username)[0] == 'oldsession'):
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
      return
#don' delete this #update_urllookup()
# update_urllookup()

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
      return render(request, 'videoplay/download.html', context1)


# Create your views here.
def home(request):
    return render(request, 'videoplay/home.html')

def play(request):
      return render(request, 'videoplay/play.html')

def temp(request):
      if request.method == 'POST':
            query = json.loads(request.POST['score'])
            print(query)
            message = "Thank You for watching! {}".format(query)
            context = {'message': message, }
            return render(request, 'videoplay/temp.html', context)
      return render(request, 'videoplay/temp.html')
