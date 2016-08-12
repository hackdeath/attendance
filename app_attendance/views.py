from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms           import UploadFileForm
from .process_file     import *

def index(request):
	form = UploadFileForm()
	return render(request, 'app_attendance/index.html', {'form': form})

def display(request):
	if request.method == 'POST':
		#Preenchendo o formulário com os dados
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			ufile = request.FILES['file']
			input = get_entradas_list(ufile.read().decode("UTF-8"))
			process(input)
			return render(request, 'app_attendance/display.html', {'input': input})
		else:
			return HttpResponse('Preenchimento do formulário inválido')
	else:
		return HttpResponse('Método de  formulário inválido')

	return HttpResponse("Hello World")
