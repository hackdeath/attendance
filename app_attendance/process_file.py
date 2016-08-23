#!/usr/bin/env python

from datetime import datetime, timedelta, date
from .models import Person, Dedada

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

    for dedada in test_list:
        if (not Person.objects.filter(id=dedada["id"])):
            criar_usuario(dedada["id"], dedada["name"])

    return test_list

def criar_usuario(id, nome):
    person = Person.objects.create(id=id, name=nome)
    person.save()

def main():
    pass

if __name__ == '__main__':
	main()
