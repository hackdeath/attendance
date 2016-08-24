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

    test_list = [{"id": person["id"], "date": person["date"], "name": person["name"]} for person in input_list]

    for person in test_list:
        person_obj = Person.objects.get(id=person["id"])
        fingerprint_obj = Fingerprint.objects.get_or_create(person=person_obj, moment=person ["date"]) # falha aqui na passagem de argumentos
        
        if (not Person.objects.filter(id=person["id"])):
            add_person(person["id"], person["name"])

        if (Person.objects.filter(id=person["id"]) and person ["date"] != fingerprint_obj.moment):
            add_moment(person_obj, person ["date"])
        
    return test_list

def add_person(id, name):
    person = Person.objects.create(id=id, name=name)
    person.save()

def add_moment (person, datetime):
    fingerprint = Fingerprint.objects.create(person=person, moment=datetime)
    fingerprint.save()

def main():
    pass

if __name__ == '__main__':
	main()
