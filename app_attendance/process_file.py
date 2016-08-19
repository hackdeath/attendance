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

    return sum_hours([person["date"] for person in input_list if person["id"] == "000000001"][1:8])
    #return [person["date"] for person in input_list if person["id"] == "000000001"][1:8]
    #return sum_hours([input_list[5], input_list[11]])

def elapsed_time(start, end):
    return (end - start)

def sum_hours(hours):
    """ Retorna a quantidade de horas 'trabalhadas' nessa lista de horários """

    splited_hours = []
    hours.reverse()

    if (len(hours) % 2 != 0):
        hours.pop()

    while(hours):
        splited_hours += [[hours.pop(), hours.pop()]]

    return [elapsed_time(period[0], period[1]) for period in splited_hours]
	
def main():
    pass

if __name__ == '__main__':
	main()
