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
                if (not last_workedtime.final and person["date"] == last_workedtime.date.date_fingerprint and last_workedtime.initial < person["time"]):
                    last_workedtime.final = person["time"]
                    last_workedtime.save()
                elif (last_workedtime.final != person["time"]):
                    worked_obj, created_worked = WorkedTime.objects.get_or_create(person=person_obj, date=date_obj, initial=person["time"])
        
    for person in person_list:
        person_obj = Person.objects.get(id=person["id"], name=person["name"])
        any_workedtime = WorkedTime.objects.filter(person=person_obj, final__isnull=True)            
        # exclui do banco de dados os dados soltos
        if (any_workedtime):
            for each in any_workedtime:
                print ("deletado")
                each.delete()

def display_input_per_day(search_form):
    init_date = search_form["init_date"]
    final_date = search_form["final_date"]
    name = search_form["name"]

    #Especificando o intervalo desejado; Especificando o nome do funcionário; Ordenando pela data
    db_data = Date.objects.filter(date_fingerprint__range=(init_date,final_date)).order_by("date_fingerprint")
    # db_data = Date.objects.filter(date_fingerprint__range=(init_date,final_date)).filter(work_times__person__name=name).order_by("date_fingerprint")

    month_name = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    if (db_data):
        current_date = db_data[0].date_fingerprint

    months = []
    days = []

    for date in db_data:
        loop_date = date.date_fingerprint
        day = generate_day_dictionary(date.worked_times, loop_date)

        if (current_date.year == loop_date.year):
            if (current_date.month == loop_date.month):
                days.append(day)
            else:
                current_date = date.date_fingerprint
                month = {"name": month_name[loop_date.month], "days": days}
                months.append(month)

                #Resetando variáveis
                days = [day]
        else:
            year = {"year": loop_date.year, "months": months}
            
            #Resetando variáveis
            months = []
            days = [day]

def generate_day_dictionary(worked_times, date):
    weekday = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    people = []
    
    for wt in date.work_times:

    person = {  "id": wt.person.id,
                "name": wt.person.name,
                "time": wt.calc_timedelta()}
    people.append(person)
    
    day = { "day": date.day,
        "weekday": weekday[date.weekday()],
        "people": people}
    
    return day