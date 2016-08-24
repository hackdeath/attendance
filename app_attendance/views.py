from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms           import UploadFileForm, SearchWorkedTimeForm
from .process_file    import *
import datetime

# To do list:
# Implementar o retorno ao index quando o formulário estiver inválido
# Construir view de confirmação quando um arquivo log for enviado
# Trocar o retorno de index()
def index(request):
	#Checando se o método do formulário está correto
	if request.method == "POST":
		#Preenchendo variáveis com os 
		file_form = UploadFileForm(request.POST, request.FILES, prefix="file")
		search_form = SearchWorkedTimeForm(request.POST, prefix="search")
		if file_form.is_valid():
			ufile = request.FILES['file']
			input = get_input(ufile.read().decode("UTF-8"))
			return HttpResponse("Upload do arquivo log feito com sucesso.")

		elif search_form.is_valid():
			return HttpResponse("Busca pronta para ser efetuada")
	
	file_form = UploadFileForm(prefix="file")
	search_form = SearchWorkedTimeForm(prefix="search")
	form = {"file": file_form, "search": search_form}
	
	return render(request, 'app_attendance/index.html', {'form': form})		






	form = {"file": file_form, "search": search_form}
	return render(request, 'app_attendance/index.html', {'form': form})

def display_per_month(request):
	if request.method == 'POST':
		#Preenchendo o formulário com os dados
		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():
			ufile = request.FILES['file']
			input = get_input(ufile.read().decode("UTF-8"))
			initDate = datetime.datetime(2016,1,1)
			finalDate = datetime.datetime.today()
			input = filter_by_period(input, initDate, finalDate)
			return render(request, 'app_attendance/display.html', {'months': input})
		else:
			return HttpResponse('Preenchimento do formulário inválido')
	else:
		return HttpResponse('Método de  formulário inválido')

def display_per_day(request):
	return HttpResponse("Ainda não foi feito")