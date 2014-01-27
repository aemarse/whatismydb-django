from django import forms
from django.core.exceptions import ValidationError

CHOICES = (('Minute', 'Hour', 'Day'))

class GetDataForm(forms.Form):
	update_rate = forms.ChoiceField(choices=CHOICES)
	start_time = forms.DateTimeField(input_formats="%m/%d/%y %H:%M")
	end_time = forms.DateTimeField(input_formats="%m/%d/%y %H:%M")