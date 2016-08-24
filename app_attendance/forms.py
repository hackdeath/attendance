from django import forms
from datetime import datetime, date

# Modificando o type no html do formulário
class DateWidget(forms.DateInput):
	input_type = "date"

class SearchWorkedTimeForm(forms.Form):
	init_date = forms.DateField(label="Início:", widget=DateWidget(), required=False)
	final_date = forms.DateField(label="Final:", widget=DateWidget(), required=False)
	name = forms.CharField(label="Nome", required=False)

class UploadFileForm(forms.Form):
	file = forms.FileField()