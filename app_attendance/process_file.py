#!/usr/bin/env python

from datetime import datetime, timedelta, date
from .models import *

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
        
        #if (created_fingerprint):
        person_filtered_start = Fingerprint.objects.filter(person=person["id"], moment=person["date"], workedtime_start__isnull=True)
        person_filtered_finish = Fingerprint.objects.filter(person=person["id"], moment=person["date"], workedtime_finish__isnull=True)
        print (person_filtered_start)
        # if (person_filtered_start.exists()):
        #     if (person_filtered_finish.exists()):
        #         WorkedTime.objects.get_or_create(start=fingerprint_obj)
        #     if (not person_filtered_finish.exists()):
        #         WorkedTime.objects.filter(start=FILTRO AQUI REVERSO).latest('start').update(finish=fingerprint_obj)
            #print (person_filtered_finish.exists())
        
            #WorkedTime.objects.filter(start=fingerprint_obj, finish__isnull=True).update(finish=fingerprint_obj)
                #WorkedTime.objects.filter(start_id=person["id"]).update(finish=fingerprint_obj)
            #WorkedTime.objects.filter(start_id=person["id"]).update(start=fingerprint_obj)
        
    return person_list

def main():
    pass

if __name__ == '__main__':
	main()

# nova_dedada do usuario x
# ultimo workedTime do usuario x

# se ultimo workedTime do usuario x tem finish
#     cria novo workedtime e joga essa nova dedada no start do usuario x

# se ultimo workedTime do usuario x nao exist
#   cria  workedTime do usuario x e joga dedada no start

# senao
#     joga essa nova dedada no finish do ultimo workedTime do usuario x