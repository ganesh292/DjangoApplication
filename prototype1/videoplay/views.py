import os
import json
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from videoplay.models import ScoreOneStimulus, VideoUrl,ScoreTwoStimulus
from user import views as user_views
from django.template import loader
import re
from django.shortcuts import redirect
username = ''
stat_url = ["{% static url%}"]

#Jatin's Backend code
video_lists = ['0000001', '0000002','0000003']
video_lists2 = [('0000001', '0000004'),('0000002','0000004')]
# jatin's changes moving to master

def checkUserExists_1(username):
	#To check if newuser or existing user?- For Single Stimulus
	obj = ScoreOneStimulus.userScore.filter(user_name=username)
	if(len(obj) == 0):
		return False
	else:
		return True
def checkUserExists_2(username):
	#To check if newuser or existing user?- For Double Stimulus
	obj = ScoreTwoStimulus.userPref.filter(user_name=username)
	if(len(obj) == 0):
		return False
	else:
		return True
def NewEntry_1(username,video_lists, sid=1):
	#To insert initial data into the table for single stimulus

      for item in video_lists:
            print("Inside NewEntry Function and gonna add ", item, "\n")
            obj = ScoreOneStimulus(
            	user_name=username, session_id=sid, vid_id=item)
            obj.save()
      return video_lists
def NewEntry_2(username,video_lists2, sid=1):
	#To insert initial data into the table for double stimulus

      for item in video_lists2:
            print("Inside NewEntry Function and gonna add ", item[0],item[1], "\n")
            obj = ScoreTwoStimulus(
            	user_name=username, session_id=sid, vid_id1=item[0],vid_id2=item[1])
            obj.save()
      return video_lists2
# NewEntry_2("abcd1")

def checkSession_1(username):
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

def checkSession_2(username):
	#To check if its new session or old session for double stimulus
	obj = ScoreTwoStimulus.userPref.filter(user_name=username).filter(preference__isnull=True)
	if(len(obj) == 0):
		return ('newsession', 'Dummy','Dummy')        
	else:
            # print(obj)
		vid_sublist = []
		for item in obj:
			vid_sublist.append((item.vid_id1,item.vid_id2))
		return ('oldsession', vid_sublist)
# print("Checking Session for double stimulus\n",checkSession_2('abcd1')[1])
def incSessionId_1(username):
	#To increment sessionid after fetching last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return (obj.session_id + 1)
def incSessionId_2(username):
	#To increment sessionid after fetching last session id
	obj = ScoreTwoStimulus.userPref.filter(
		user_name=username).order_by('-session_id')[0]
	return (obj.session_id + 1)

def findSessionId_1(username):
	#To find last session id
	obj = ScoreOneStimulus.userScore.filter(
		user_name=username).order_by('-session_id')[0]
	return obj.session_id
def findSessionId_2(username):
	#To find last session id
	obj = ScoreTwoStimulus.userPref.filter(
		user_name=username).order_by('-session_id')[0]
	return obj.session_id
# print("SessionId2\t",findSessionId_2('abcd1'))
# print("SessionId2\t",incSessionId_2('abcd1'))
def updateScore_1(username, sid, vid, scr):
	# To update score in the database table
      obj = ScoreOneStimulus.userScore.get(user_name=username, session_id=sid, vid_id=vid)
      obj.score = scr
      obj.save()
      print("Score updated in backend Bingo!!!")
      return
def updatePref_2(username, sid, vid1,vid2, pref):
	# To update score in the database table
      print(username)
      print(sid)
      print(vid1)
      print(vid2)
      obj = ScoreTwoStimulus.userPref.get(user_name=username, session_id=sid, vid_id1=vid1,vid_id2=vid2 )
      obj.preference = pref
      obj.save()
      print("Pref is updated in backend Bingo!!!")
      return
# updatePref_2('abcd121',1,'0000003','0000001','0000003')
def backendlogic_1(username):
      # For Single Stimulus
      if checkUserExists_1(username) == False:
            NewEntry_1(username,video_lists)
            return video_lists
      else:
            if(checkSession_1(username)[0] == 'oldsession'):
                  return checkSession_1(username)[1]
            else:
                  sid = incSessionId_1(username)
                  return NewEntry_1(username,video_lists, sid)
def backendlogic_2(username):
      # For Double Stimulus
      if checkUserExists_2(username) == False:
            NewEntry_2(username,video_lists2)
            return video_lists2
      else:
            if(checkSession_2(username)[0] == 'oldsession'):
                  return checkSession_2(username)[1]
            else:
                  sid = incSessionId_2(username)
                  return NewEntry_2(username,video_lists2, sid)

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

def getvid(videoname):
      #To get vid id from database for given video name"
      print("Given below is the url for reverselookup")
      print('http://vision-pc4.eng.uwaterloo.ca:/videos/'+videoname)
      vid=VideoUrl.urlobj.get(vid_url='http://vision-pc4.eng.uwaterloo.ca:/videos/'+videoname).vid_id
      print(vid)
      return vid
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
      video_lists1 = backendlogic_1(request.user)
      print(video_lists2)
      # urls = fetchVideo(video_lists1)
      # print(urls)
      context1 = {}
      # context1['urls'] = ','.join([str(i) for i in urls])
      return render(request, 'videoplay/download.html', context1)


# Create your views here.
def home(request):
    return render(request, 'videoplay/home.html')

def play(request):
      if request.method == 'POST':
            query = json.loads(request.POST['score'])
            query1=(request.POST['fileName'])
            print(query)
            print(query1)
            updateScore_1(request.user, findSessionId_1(request.user), getvid(query1), query)
            message = "Thank You for watching! {}".format(query)
            context = {'message': message, }
            return render(request, 'videoplay/play.html', context)
      return render(request, 'videoplay/play.html')
def play2(request):
      if request.method == 'POST':
            # query = json.loads(request.POST['score'])
            # query1=(request.POST['fileName'])
            vid1=getvid(request.POST['vid_name1'])
            vid2=getvid(request.POST['vid_name2'])
            print(vid1)
            print(vid2)
            print(request.user)
            pref=json.loads(request.POST['preference'])
            # updatePref_2(request.user, 1, vid1,vid2, vid1)
            if(pref=='1'):
                  updatePref_2(request.user, 1, vid1,vid2, vid1)
                  print("Bingo")
            elif(pref=='2'):
                  updatePref_2(request.user, 1, vid1,vid2, vid2)
                  print('bingo!')
            else:
                  print("Enter Wrong Preference")
            # print(query)
            # print(query1)
            
            # updateScore_1(request.user, findSessionId_1(request.user), getvid(query1), query)
            message = "Thank You for watching!"
            context = {'message': message, }
            return render(request, 'videoplay/play2.html', context)
      return render(request, 'videoplay/play2.html')

def temp(request):
      # if request.method == 'POST':
      #       query = json.loads(request.POST['score'])
      #       print(query)
      #       message = "Thank You for watching! {}".format(query)
      #       context = {'message': message, }
      #       return render(request, 'videoplay/temp.html', context)
      return render(request, 'videoplay/temp.html')
