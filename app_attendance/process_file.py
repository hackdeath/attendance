#!/usr/bin/env python

from datetime import *

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

    return input_list	

inputs = [
	{"id": 1, "name": "a"},
	{"id": 2, "name": "b"},
	{"id": 2, "name": "c"},
	{"id": 3, "name": "d"},
	{"id": 3, "name": "e"},
	{"id": 3, "name": "f"},
	{"id": 4, "name": "g"},
	{"id": 4, "name": "h"},
	{"id": 4, "name": "i"},
	{"id": 4, "name": "j"},
	{"id": 5, "name": "k"},
	{"id": 5, "name": "l"},
	{"id": 5, "name": "m"},
	{"id": 5, "name": "n"},
	{"id": 5, "name": "o"}
]

def split_people():
	""" Divide pessoas em vetores """

	ids_list = []
	for i in inputs:
		ids_list.append(i["id"])

	ids_set = set(ids_list)

	splited_person = []

	for i in ids_set:
		splited_people = []
		while j < len(inputs):
			if i == inputs[j]["id"]:
				splited_people.append(obj)
				del inputs[j]
				
			j += 1

		splited_person.append(splited_people)
	# for i in range(len(inputs)):
	# 	#Separando um id para buscar
	# 	id = inputs[i]["id"]

	# 	#Iniciando a lista temporária dos dados de um único id
	# 	splited_people = []
	# 	#Percorrendo os valores disponíveis para achar os dados do id escolhido 
	# 	for obj in inputs:
	# 		print ("id = {0} | i = {1} | obj = {2}".format(id,i,obj))
	# 		if id == obj["id"]:
	# 			splited_people.append(obj)

	# 	for j, obj in enumerate(inputs):
	# 		if id == obj["id"]:
	# 			del inputs[j]
	# 			print ("Deletei | {0}".format(j))
	# 	#Adicinando a lista de um id à lista geral
	# 	splited_person.append(splited_people)

	return splited_person

def main():
    print (split_people())

if __name__ == '__main__':
	main()