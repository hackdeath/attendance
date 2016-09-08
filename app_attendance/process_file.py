#!/usr/bin/env python

from datetime import datetime, timedelta, date, time
from .models import *
from django.utils import dateparse

def get_input(inFile):
    # Lê arquivo ignorando primeira e última linhas
    inFile = inFile.split('\n')[1:-1]
    
    #lista de entradas (ponto)
    input_list = []
    for line in inFile:
        splited_line = line.split("\t")
        splited_datetime = splited_line[4][:-1].split("  ")
        time = dateparse.parse_time(splited_datetime[1])
        date = datetime.strptime(splited_line[4][:-1], "%Y/%m/%d %H:%M").date()
        item = {"id": splited_line[2], "name": splited_line[3].strip(), "date": date, "time": time}
        input_list.append(item)

    # adicionado key "time"
    person_list = [{"id": person["id"], "date": person["date"], "name": person["name"], "time": person["time"]} for person in input_list]

    for person in person_list:
        person_obj, created_person = Person.objects.get_or_create(id=person["id"], name=person["name"])
        date_obj, created_dates = Date.objects.get_or_create(date_fingerprint=person["date"])

        # criar uma linha para "pessoa"
        if (created_person):
            WorkedTime.objects.create(person=person_obj, date=date_obj, initial=person["time"]).save()

        # adicionar "time" no initial ou final
        else:
            # filtra última ocorrência e pega o objeto (esse filtro tem problemas)
            last_workedtime = WorkedTime.objects.filter(person=person_obj).order_by('-person', '-date').latest('initial')
            if (last_workedtime):
                if(not last_workedtime.final):
                    last_workedtime.final = person["time"]
                    last_workedtime.save()
                else:
                    worked_obj, created_worked = WorkedTime.objects.get_or_create(person=person_obj, date=date_obj, initial=person["time"])

def display_input(search_form, mode):
    init_date = search_form["init_date"]
    final_date = search_form["final_date"]
    id = search_form["id"]

    #Especificando o intervalo desejado
    db_data = Date.objects.filter(date_fingerprint__range=(init_date,final_date))
    #Especificando o nome do funcionário
    db_data = db_data.filter(work_times__person__id=id)
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
                    #Criando dicionário para o dia
                    day = { "day": splited_day.day,
                            "weekday": weekday[splited_day.weekday()],
                            "people": generate_people_list(splited_day.worked_times)}
                    days.append(day)

                #Criando dicionário para o mês
                month = {   "name": month_name[current_month.month - 1],
                            "days": days}

            #Gerando dados por mês
            else if(mode == "month"):
                people = []
                #Os meses já separam os dias
                for splited_day in splited_month:
                    people = people + generate_people_list(splited_day.worked_times)

                month = {   "name": month_name[current_month.month - 1]
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
    people = []
    
    for worked_time in worked_times:
        person = {  "id": worked_time.person.id,
                    "name": worked_time.person.name,
                    "time": worked_time.calc_timedelta()}
        people.append(person)

    return people
