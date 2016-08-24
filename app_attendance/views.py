from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms           import UploadFileForm
from .process_file    import *
from datetime         import timedelta

def index(request):
    form = UploadFileForm()
    return render(request, 'app_attendance/index.html', {'form': form})

def display(request):
    if request.method == 'POST':
        #Preenchendo o formulário com os dados
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            ufile = request.FILES['file']
            ################# Para teste #################

            # por mes

            # joao    = {"id": 1, "name": "joao", "time": timedelta(hours=32)}
            # sabrina = {"id": 2, "name": "sabrina", "time": timedelta(hours=57)}
            # hugo    = {"id": 3, "name": "hugo", "time": timedelta(days=2)}
            # dilma   = {"id": 4, "name": "dilma", "time": timedelta(hours=9)}
            # people  = [joao, sabrina, hugo, dilma]

            # janeiro   = {"name": "janeiro", "people": people}
            # fevereiro = {"name": "fevereiro", "people": people}
            # março     = {"name": "março", "people": people}
            # abril     = {"name": "abril", "people": people}
            # months    = [janeiro, fevereiro, março, abril]

            # year_2014 = {"year": 2014, "months": months}
            # year_2015 = {"year": 2015, "months": months}
            # year_2016 = {"year": 2016, "months": months}
            # years = [year_2014, year_2015, year_2016]

            # data = years
            ################# Para teste #################
            # por dia

            # joao    = {"id": 1, "name": "joao", "time": timedelta(hours=5)}
            # sabrina = {"id": 2, "name": "sabrina", "time": timedelta(hours=50)}
            # hugo    = {"id": 3, "name": "hugo", "time": timedelta(hours=2)}
            # dilma   = {"id": 4, "name": "dilma", "time": timedelta(hours=9)}
            # people  = [joao, sabrina, hugo, dilma]

            # day_01 = {"day": 1, "weekday": "Segunda", "people": people}
            # day_02 = {"day": 2, "weekday": "Terça", "people": people}
            # day_03 = {"day": 3, "weekday": "Quarta", "people": people}
            # day_04 = {"day": 4, "weekday": "Quinta", "people": people}
            # day_05 = {"day": 5, "weekday": "Sexta", "people": people}
            # day_06 = {"day": 6, "weekday": "Sábado", "people": people}
            # day_07 = {"day": 7, "weekday": "Domingo", "people": people}
            # day_08 = {"day": 8, "weekday": "Segunda", "people": people}
            # day_09 = {"day": 9, "weekday": "Terça", "people": people}
            # day_10 = {"day": 10, "weekday": "Quarta", "people": people}
            # day_11 = {"day": 11, "weekday": "Quinta", "people": people}
            # days = [day_01, day_02, day_03, day_04, day_05, day_06, day_07, day_08, day_09, day_10, day_11]

            # janeiro   = {"name": "janeiro", "days": days}
            # fevereiro = {"name": "fevereiro", "days": days}
            # março     = {"name": "março", "days": days}
            # abril     = {"name": "abril", "days": days}
            # months    = [janeiro, fevereiro, março, abril]

            # year_2014 = {"year": 2014, "months": months}
            # year_2015 = {"year": 2015, "months": months}
            # year_2016 = {"year": 2016, "months": months}
            # years = [year_2014, year_2015, year_2016]

            # data = years
            ################# Para teste #################
            return render(request, 'app_attendance/display_day.html', {'data': data})
        else:
            return HttpResponse('Preenchimento do formulário inválido')
    else:
        return HttpResponse('Método de  formulário inválido')

    return HttpResponse("Hello World")
