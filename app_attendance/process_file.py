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
        
        if (created_fingerprint):
            if (not WorkedTime.objects.filter(id=person["id"]).exists()):
                workedTime_obj, created_workedTime_start = WorkedTime.objects.get_or_create(start=fingerprint_obj)
            
            elif (WorkedTime.objects.filter(id=person["id"]).latest('id').finish is None): # se o ultimo finish workedTime do usuario está vazio
                workedTime_obj, created_workedTime_start = WorkedTime.objects.get_or_create(start=fingerprint_obj)

            else:
                workedTime_obj = WorkedTime.objects.get(id=person["id"])
                workedtime.finish = fingerprint_obj
                workedtime.save() 


        #else if():
        #     workedTime_obj, created_workedTime_finish = WorkedTime.objects.get_or_create(finish=fingerprint_obj)

    return person_list

def main():
    pass

if __name__ == '__main__':
	main()

# nova_dedada do usuario x
# ultimo workedTime do usuario x


# se ultimo workedTime do usuario x nao exist
#   cria  workedTime do usuario x e joga dedada no start

# se ultimo workedTime do usuario x tem finish
#     cria novo workedtime e joga essa nova dedada no start do usuario x

# senao
#     joga essa nova dedada no finish do ultimo workedTime do usuario x