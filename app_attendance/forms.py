from django import forms
from datetime import datetime, date

# Modificando o type no html do formulário
class DateWidget(forms.DateInput):
	input_type = "date"

class SearchWorkedTimeForm(forms.Form):
	init_date  = forms.DateField(label="Início:", widget=DateWidget(), required=False, initial=date(date.today().year, 1, 1))
	final_date = forms.DateField(label="Final:",  widget=DateWidget(), required=False, initial=date.today())
	id       = forms.IntegerField(label="ID:", required=False)

class UploadFileForm(forms.Form):
	file = forms.FileField()
