#!/usr/bin/env python

from datetime import datetime, timedelta, date, time
from .models import *
from django.utils import dateparse

def get_input(inFile):
    # Lê arquivo ignorando primeira e última linhas
    inFile = inFile.split('\n')[1:-1]
    
    #lista de entradas (ponto)
    person_list = []

    for line in inFile:
        splited_line = line.split("\t")
        splited_datetime = splited_line[4][:-1].split("  ")
        time = dateparse.parse_time(splited_datetime[1])
        date = datetime.strptime(splited_line[4][:-1], "%Y/%m/%d %H:%M").date()
        item = {"id": splited_line[2], "name": splited_line[3].strip(), "date": date, "time": time}
        person_list.append(item)

    for person in person_list:
        person_obj, created_person = Person.objects.get_or_create(id=person["id"], name=person["name"])
        date_obj, created_dates = Date.objects.get_or_create(date_fingerprint=person["date"])
        
        # criar uma linha para "pessoa"
        if (created_person):
            WorkedTime.objects.create(person=person_obj, date=date_obj, initial=person["time"]).save()

        # adicionar "time" no initial ou final
        else:
            # filtra última ocorrência da determinada pessoa
            last_workedtime = WorkedTime.objects.filter(person=person_obj).order_by('-date', '-initial')
            if (last_workedtime.exists()):
                # pega o objeto da pessoa filtrada
                last_workedtime = last_workedtime.latest('initial')
                # checa se deve atualizar o final
                if (not last_workedtime.final and person["date"] == last_workedtime.date.date_fingerprint and last_workedtime.initial < person["time"]):
                    last_workedtime.final = person["time"]
                    last_workedtime.save()
                # cria uma nova row preenchendo o initial
                elif (last_workedtime.final != person["time"]):
                    worked_obj, created_worked = WorkedTime.objects.get_or_create(person=person_obj, date=date_obj, initial=person["time"])
    
    # exclui os dados não pareados
    for person in person_list:
        person_obj = Person.objects.get(id=person["id"], name=person["name"])
        any_workedtime = WorkedTime.objects.filter(person=person_obj, final__isnull=True)            
        date_orphan = Date.objects.filter(worked_times=None)
        for each in any_workedtime:
            each.delete()
        for date in date_orphan:
            date.delete()

def display_input(search_form, mode):
    #Preenchendo valor de init_date
    if (search_form["init_date"] == None): init_date = date.min
    else: init_date = search_form["init_date"]

    #Preenchendo valor de final_date
    if (search_form["final_date"] == None): final_date = date.max
    else: final_date = search_form["final_date"]
    

    #Especificando o intervalo desejado
    db_data = Date.objects.filter(date_fingerprint__range=(init_date,final_date))
    #Selecionando as datas que contenham worked_times com id especificado
    #Otimiza o processamento dos dados
    if (search_form["id"] != None):
        id = search_form["id"]
        db_data = db_data.filter(worked_times__person__id__exact=id).distinct()
    #Ordenando pela data
    db_data = db_data.order_by("date_fingerprint")

    #Definindo as variáveis gerais usadas no algoritmo
    data = [] #Variável final de retorno
    month_name = [  "Janeiro",
                    "Fevereiro",
                    "Março",
                    "Abril",
                    "Maio",
                    "Junho",
                    "Julho",
                    "Agosto",
                    "Setembro",
                    "Outubro",
                    "Novembro",
                    "Dezembro"]

    weekday = [ "Segunda-feira",
                "Terça-feira",
                "Quarta-feira",
                "Quinta-feira",
                "Sexta-feira",
                "Sábado",
                "Domingo"]

    #Coletando os anos possíveis no db_data
    year_list = db_data.dates("date_fingerprint", "year", order="ASC")
    for current_year in year_list:
        splited_year = db_data.filter(date_fingerprint__year=current_year.year)
        
        months = []
        #Coletando meses possíveis no splited_year
        month_list = splited_year.dates("date_fingerprint","month", order="ASC")
        for current_month in month_list:
            splited_month = splited_year.filter(date_fingerprint__month=current_month.month)
            #Gerando dados por dia
            if (mode == "day"):
                days = []
                #Os meses já separam os dias
                for splited_day in splited_month:
                    print ("Hello world")
                    print (splited_month)
                    worked_times = splited_day.worked_times.select_related()
                    #Filtrando os worked_times por id
                    if (search_form["id"] != None): 
                        worked_times = worked_times.filter(person__id__exact=id)

                    weekday_number = splited_day.date_fingerprint.weekday()
                    #Criando dicionário para o dia
                    day = { "day": splited_day.date_fingerprint.day,
                            "weekday": weekday[weekday_number],
                            "people": generate_people_list(worked_times)}
                    days.append(day)

                #Criando dicionário para o mês
                month = {   "name": month_name[current_month.month - 1],
                            "days": days}

            #Gerando dados por mês
            elif (mode == "month"):
                people = []
                #Os meses já separam os dias
                for splited_day in splited_month:
                    worked_times = splited_day.worked_times.select_related()
                    #Filtrando os worked_times por id
                    if (search_form["id"] != None):
                        worked_times = worked_times.filter(person__id__exact=id)
                    
                    people = people + generate_people_list(worked_times)

                month = {   "name": month_name[current_month.month - 1],
                            "people": people}

            #Caso mode não seja 'day' ou 'month', retornar lista vazia
            else:
                return []


            months.append(month)

        #Criando dicionário para o ano
        year = {"year": current_year.year,
                "months": months}
        data.append(year)

    return data

def generate_people_list(worked_times):
    list_people = []

    for wt in worked_times: list_people.append(worked_times.person)

    set_people = set(list_people)
    people = []
    for set_person in set_people:
        person_wt = worked_times.filter(person=set_person)

        total_time = timedelta(seconds=0)
        for i in person_wt: total_time = total_time + i.calc_timedelta()

        person = {  "id": person_wt.person.id,
                    "name": person_wt.person.name,
                    "time": total_time}
        people.append(person)

    return people
