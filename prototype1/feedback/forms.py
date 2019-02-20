from django import forms
from feedback.models import ScoreOneStimulus

class ScoreForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your score on scale of 1 to 10..'}))

	class Meta:
		model = ScoreOneStimulus	
		fields= ['score']
		widgets={'score':forms.HiddenInput()}



