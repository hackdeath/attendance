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