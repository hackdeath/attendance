#!/usr/bin/env python

from datetime import datetime, timedelta, date
from .models import *
from django.db.models import Q

def get_input(inFile):
    # Lê arquivo ignorando primeira e última linhas
    inFile = inFile.split('\n')[1:-1]
    
    #lista de entradas (ponto)
    input_list = []
    for line in inFile:
        splited_line = line.split("\t")
        date = datetime.strptime(splited_line[4][:-1], "%Y/%m/%d  %H:%M")
        item = {"id": splited_line[2], "name": splited_line[3].strip(), "date": date}
        input_list.append(item)

    person_list = [{"id": person["id"], "date": person["date"], "name": person["name"]} for person in input_list]

    for person in person_list:
        person_obj, created_person = Person.objects.get_or_create(id=person["id"], name=person["name"])
        fingerprint_obj, created_fingerprint = Fingerprint.objects.get_or_create(person=person_obj, moment=person["date"])
        
        if (created_person):
            WorkedTime.objects.create(start=fingerprint_obj).save()

        elif (created_fingerprint):
            penult_fingerprint = Fingerprint.objects.filter(person = person_obj).order_by('-moment')[1]
            exists_workedtime  = WorkedTime.objects.get(Q(start = penult_fingerprint) | Q(finish = penult_fingerprint))

            if (exists_workedtime):
                if (not exists_workedtime.finish and penult_fingerprint.moment.date() == fingerprint_obj.moment.date()):
                    exists_workedtime.finish = fingerprint_obj
                    exists_workedtime.save()
                else:
                    WorkedTime.objects.create(start=fingerprint_obj).save()

def display_input_per_day(search_form):
    init_date = search_form["init_date"]
    final_date = search_form["final_date"]
    name = search_form["name"]

    #Especificando o intervalo desejado; Especificando o nome do funcionário; Ordenando pela data
    db_data = WorkedTime.objects.filter(start__moment__range=(init_date,final_date)).filter(start__person__name=name).order_by("start__moment")

    #Lista final
    data = []
    #Lista temporário para guardar os dados separados por período
    months = []
    days = []
    people = []
    #Listas para conversão
    weekday = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    month_name = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    #Inicializando variáveis current's com o primeiro datetime
    current_year = db_data[0].start.moment.year
    current_month = db_data[0].start.moment.month
    current_day = db_data[0].start.moment.day
    #Separando por anos
    print (db_data)############################################################################################################################################
    for worked_time in db_data:
        moment = worked_time.start.moment
        print ("Date: {0}".format(moment))##############################################################################################################################
        #Separando por anos
        if (current_year == moment.year):
            #Separando por meses
            if (current_month == moment.month):
                #Formatando dados de uma pessoa
                person = {  "id":   worked_time.start.person.id,
                            "name": worked_time.start.person.name,
                            "time": worked_time.calc_timedelta()
                }
                print ("Person: {0}".format(person)) ######################################################################################################
                #Separando por dias
                if (current_day == moment.day):
                    people.append(person)
                #Não há mais fingerprints com current_day associado à current_month e current_year em db_data
                else:
                    #Formatando dados de um dia
                    day = { "day":      current_day,
                            "weekday":  weekday[moment.weekday()],
                            "people":   people
                    }
                    #Adicionar day em days
                    print ("Day: {0}".format(day)) ######################################################################################################
                    days.append(day)
                    people = [person]
                    current_day = moment.day

            #Não há mais fingerprints com current_month associado à current_year em db_data
            else:
                #Formatando dados de um mês
                month = {   "name": month_name[current_month],
                            "days": days
                }
                print ("Month: {0}".format(month)) ######################################################################################################
                #Adicionar month em months
                months.append(month)
                days = []
                current_month = moment.month

        #Não há mais fingerprints com current_year em db_data
        else:
            year = {"year": current_year,
                    "months": months
            }
            print ("Year: {0}".format(year)) ######################################################################################################
            #Adicionar year em data
            data.append(year)
            months = []
            current_year = moment.year

    return data

def display_input_per_month(search_form):
    return []