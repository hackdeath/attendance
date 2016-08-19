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

    # Código abaixo para testes
    #return sum_hours([person["date"] for person in input_list if person["id"] == "000000001"][1:8])
    #return [person["date"] for person in input_list if person["id"] == "000000001"][1:8]

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
	
def main():
    pass

if __name__ == '__main__':
	main()
