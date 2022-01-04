from django import forms
from formsapp.models import FormDetails

class FormDetailsForm(forms.ModelForm):
	class Meta:
		model = FormDetails
		fields = '__all__'