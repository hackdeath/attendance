#!/usr/bin/env python

from datetime import datetime, timedelta, date

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

	today = date.today()
	last_week = today - timedelta(days=80)
	#print(today)
	#print(last_week)

	#test_list = [{"id": person["id"], "date": person["date"]} for person in input_list if person["id"] == "000000001"][1:8]
	#test_list = [{"id": person["id"], "date": person["date"]} for person in input_list if person["date"] > last_week]
	test_list = [{"id": person["id"], "date": person["date"], "name": person["name"]} for person in input_list]
	return test_list

def filter_by_period (inputs, init_date, final_date):
	select_inputs = []
	for i in inputs:
		if (init_date < i["date"] < final_date):
			select_inputs.append(i)

	f_inputs = []
	f_inputs.append([])
	count_list = 0
	last_date = select_inputs[0]["date"]
	for i in select_inputs:
		if (i["date"].year == last_date.year and i["date"].month == last_date.month):
			f_inputs[count_list].append(i)
		else:
			count_list += 1
			f_inputs.append([])
			f_inputs[count_list].append(i)
			last_date = i["date"]


	return list(map(split_people, f_inputs))
	#return split_people(select_inputs)

def sum_hours_person(person_list):
	""" Soma a quantidade de horas 'trabalhadas' por uma pessoa """

	#print("Arthur: {0}".format(person_list))
	date_list = [item["date"] for item in person_list]

	start = date_list[0]
	final = date_list[-1]
	
	qt_hours = {"id": person_list[0]["id"], "period": (str(start), str(final)), "quantity": sum_hours(date_list), "name": person_list[0]["name"]}

	return qt_hours

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

	return str(sum(timedeltas, timedelta()))

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
		while j < len(inputs):
			if i == inputs[j]["id"]:
				splited_person.append(inputs[j])
				del inputs[j]
				j -= 1
			j += 1

		splited_people.append(splited_person)

	#print("Antonio: {0}".format(splited_people))
	return list(map(sum_hours_person, splited_people))