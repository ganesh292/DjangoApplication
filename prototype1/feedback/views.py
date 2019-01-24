# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from feedback.forms import ScoreForm
# Create your views here.
class score(TemplateView):
 	template_name = 'sample.html'
	
	def get(self, request):
		form = ScoreForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = ScoreForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = ScoreForm()
			return redirect('sample')
		args = {'form': form, 'text' : text}	
		return render(request, self.template_name, args)



