from django import forms 
from django.forms import ModelForm
from .models import (CompanyEmail1)
import datetime 

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.Form):
	company_name = forms.CharField()
	location = forms.CharField()
	email_address = forms.EmailField()
	password = forms.CharField()
	subject = forms.CharField()
	application_date = forms.DateInput()

# Create the form class.
class ApplicationModelForm(forms.ModelForm):
	class Meta:
		model = CompanyEmail1
		fields = ['company_name','location','application_date','email_address']
		widgets = {'application_date': DateInput(),}