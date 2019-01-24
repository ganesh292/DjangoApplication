# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from feedback.forms import ScoreForm
# Create your views here.
def score(request):
    return render(request,'sample.html')


def get(request):
	form = ScoreForm()
	return render(request,'sample.html', {'form':form})

def post(request):
	form = ScoreForm(request.POST)
	if form.is_valid():
		post = form.save(commit=False)
		post.user = request.user
		post.save()
		text = form.cleaned_data['post']
		form = ScoreForm()
		return redirect('sample')
	args = {'form': form, 'text' : text}	
	return render(request,'sample.html', args)



