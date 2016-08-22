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

	splited_people = []

	for i in ids_set:
		splited_person = []
		j = 0
		print(splited_people)
		while j < len(inputs):
			print ("j = {0} | len(inputs) = {1} | id = {2} | i = {3}".format(j, len(inputs), inputs[j]["id"],  i))
			if i == inputs[j]["id"]:
				splited_person.append(inputs[j])
				del inputs[j]
				j -= 1
			j += 1

		splited_people.append(splited_person)

	return splited_people

def main():
    print (split_people())

if __name__ == '__main__':
	main()