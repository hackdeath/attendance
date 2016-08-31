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

    x = WorkedTime.objects.filter(start__moment__range=(init_date,final_date)).filter(start__person__name=name)

    print (x[0].start.moment.date())
    output_data = []
    return output_data

def display_input_per_month(file_form):
    pass