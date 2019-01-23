# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.
def score(request):
    return render(request,'feedback/sample.html')
def score_submission(request):
    print("Hello score is uploaded")
    score= request.POST["score_input"]
    rating= score(score_input=score)
    rating.save()
    return render(request,'feedback/sample.html')


