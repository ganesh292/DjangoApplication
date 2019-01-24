from django import forms
from feedback.models import score

class ScoreForm(forms.ModelForm):
	post = forms.CharField()

	class Meta:
		model = score	
		fields= ('score_input',)