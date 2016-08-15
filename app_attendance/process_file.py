#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2016 Batalha <batalha@EliteDesk>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from datetime import datetime, date

def get_entradas_list(inFile):
	#lendo a primeira linha, que não é utilizada.
	inFile = inFile.split('\n')[1:]


	#lista de entradas (ponto)
	entradas = []
	for line in inFile:
		splited_line = line.split("\t")
		dt = datetime.strptime(splited_line[4][:-2], "%Y/%m/%d  %H:%M")
		
		d = {"id": splited_line[2], "name": splited_line[3].strip(), "date": dt}
		entradas.append(d)
	return entradas	
	
def filtro(entradas, name, date):
	filtro =  filter(lambda person: person['name'] == name, entradas)
	filtro =  filter(lambda person: person['date'].date() == date, filtro)
	
	return filtro

#Código ainda não testado.
def process(input):
	fInput = []

	while input:
		#Pegando um nome não utilizado
		name = input[0]['name']
		id = input[0]['id']

		#Transferindo os dados de uma pessoa para perInput
		dateInput = []
		for i in range(len(input)):
			if input[i]['name'] == name:
				dateInput.append(input[i]['date'])
				del input[i]

		#Ordenando as datas
		dtInput.sort()

		datesList = []
		for i in dtInput:
			#Restringindo a apenas uma data
			dateSelect = []
			for j in range(len(dtInput)):
				if dtInput[i].date == dtInput[j].date:
					dateSelect = dtInput[j]
					del dtInput[j]

			#Encontrando menor horário do dia
			initTime = datetime.max
			for j in dateSelect:
				if initTime > j:
					initTime = j

			#Encontrando maior horário do dia
			finalTime = datetime.min
			for j in dateSelect:
				if finalTime < j:
					finalTime = j

			#Checando se houve apenas uma entrada e calculando timedelta
			if initTime == finalTime:
				timeDiff = timedelta(0)
			else:
				timeDiff = finalTime - initTime

			datesList = {"date": i, "hours": timeDiff}

		#salvando os dados finais para o template
		fInput.append({"id": id, "name": name, "datesList": dateInput})
	
	return fInput

def main():
	
	entradas = get_entradas_list()

	process(entradas)
	
	return 0

if __name__ == '__main__':
	main()