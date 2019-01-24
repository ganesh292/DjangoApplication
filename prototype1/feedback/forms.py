from django import froms
from feedback.models import score

class ScoreForm(forms.ModelForm):
	post = forms.IntegerField()

	class Meta:
		model = score	
		fields= ('score_input',)