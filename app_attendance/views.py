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
		#Para upload de arquivos
		file_form = UploadFileForm(request.POST, request.FILES)
		search_form = SearchWorkedTimeForm(request.POST)
		if request.POST.get("file_upload__submit"):
			#Checando se o formulário é válido
			if file_form.is_valid():
				#Fazendo upload do arquivo no banco de dados e retornando confirmação
				ufile = request.FILES['file']
				get_input(ufile.read().decode("UTF-8"))
				return render(request, 'app_attendance/confirm_file_uploaded.html')

		#Para busca por mês
		elif request.POST.get("search_per_month__submit"):
			#Checando se o formulário é válido
			if search_form.is_valid():
				data = display_input_per_month(search_form.cleaned_data)
				return display_per_month(search_form)
		#Para busca por dia
		elif request.POST.get("search_per_day__submit"):
			#Checando se o formulário é válido
			if search_form.is_valid():
				data = display_input_per_day(search_form.cleaned_data)
				print (data)
				return render(request, 'app_attendance/display_day.html', {"data": data})
	#Caso não seja, criar formulário vazio
	else:
		file_form = UploadFileForm()
		search_form = SearchWorkedTimeForm()
	
	form = {"file": file_form, "search": search_form}
	return render(request, 'app_attendance/index.html', {'form': form})
