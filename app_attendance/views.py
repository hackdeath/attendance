from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms           import UploadFileForm
from .process_file    import *
import datetime

def index(request):
	form = UploadFileForm()
	return render(request, 'app_attendance/index.html', {'form': form})

def display(request):
	if request.method == 'POST':
		#Preenchendo o formulário com os dados
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			ufile = request.FILES['file']
			input = get_input(ufile.read().decode("UTF-8"))
			initDate = datetime.datetime(2016,1,1)
			finalDate = datetime.datetime.today()
			input = filter_by_period(input, initDate, finalDate)
			return render(request, 'app_attendance/display.html', {'people': input})
		else:
			return HttpResponse('Preenchimento do formulário inválido')
	else:
		return HttpResponse('Método de  formulário inválido')

	return HttpResponse("Hello World")
