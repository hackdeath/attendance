#!/usr/bin/env python

from datetime import datetime, timedelta

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

def sum_hours(hours):
    """ Retorna a quantidade de horas 'trabalhadas' nessa lista de horários
        Por enquanto, se receber uma quantidade impar de entradas, ignora a última. """

    splited_hours = []

    if (len(hours) % 2 != 0):
        hours.pop()

    hours.reverse()

    while(hours):
        splited_hours += [[hours.pop(), hours.pop()]]

    timedeltas = [(period[1] - period[0]) for period in splited_hours]

    return sum(timedeltas, timedelta())

def split_people(inputs):
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