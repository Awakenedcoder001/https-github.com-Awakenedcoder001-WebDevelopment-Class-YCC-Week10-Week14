from django import forms
from nightapp.models import Personal_Details

class Personal_DetailsForms(forms.ModelForm):
	class Meta:
		model = Personal_Details
		fields = '__all__'