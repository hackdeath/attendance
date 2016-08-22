#!/usr/bin/env python

"""
pessoa     = {"id": int, "name": string, "date": datetime}
dt_person  = {"id": int, "date": datetime}
qt_hours   = {"id": int, "period": (datetime, datetime), "quantity": int}
hours_sum  = timedelta

#[1 1 1 1 1 2 2 2 3 3 3 4]
#[[1 1 1 1 1], [2 2 2], [3 3 3], [4]]
#[soma(1), soma(2), soma(3), soma(4)]
"""

from datetime import *

#from datetime import datetime, timedelta

# [dt_person] example
# test_list = [
#     {"id": 1, "date": datetime(2016, 7, 13, 13, 30)},
#     {"id": 1, "date": datetime(2016, 7, 13, 10, 30)},
#     {"id": 1, "date": datetime(2016, 7, 13, 18, 30)},
#     {"id": 1, "date": datetime(2016, 7, 13, 12, 30)},
# ]

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

    #return sum_hours_person(test_list)	


def sum_hours_person(test_list):
    """ Soma a quantidade de horas 'trabalhadas' por uma pessoa """

    date_list = [item["date"] for item in test_list]
    date_list.sort()

    start = date_list[0]
    final = date_list[len(date_list)-1]
    
    qt_hours = {"id": test_list[0]["id"], "period": (start, final), "quantity": sum_hours([date_list])}

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

    # Código abaixo para testes
    #return sum_hours([person["date"] for person in input_list if person["id"] == "000000001"][1:8])
    #return [person["date"] for person in input_list if person["id"] == "000000001"][1:8]

    return sum(timedeltas, timedelta())
	
def main():
    pass

if __name__ == '__main__':
	main()
