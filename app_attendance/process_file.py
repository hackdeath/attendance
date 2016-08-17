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
import itertools

def get_entradas_list(in_file):
	#lendo a primeira linha, que não é utilizada.
	in_file = in_file.split("\n")[1:-1]
	
	#lista de entradas (ponto)
	entradas = []
	for line in in_file:
		splited_line = line.split("\t")
		dt = datetime.strptime(splited_line[4][:-1], "%Y/%m/%d  %H:%M")

		d = {"id": splited_line[2], "name": splited_line[3].strip(), "date": dt}
		entradas.append(d)
	return entradas	
	
def filtro(entradas, name, date):
	filtro =  filter(lambda person: person['name'] == name, entradas)
	filtro =  filter(lambda person: person['date'].date() == date, filtro)
	
	return filtro

def process(entradas):
	entradas_list = [];
	
	for item in entradas:
	#	print "--------------", item["id"], item["name"],item["date"]
		sub_filtro = []
		sub_filtro = filtro(entradas, item["name"], item["date"].date())
					
		for thing in sub_filtro:
			if not(thing in entradas_list):
				entradas_list.append(thing)

	for x, y in zip(entradas_list, entradas_list):
		print("Current: {0}\nNext: {1}".format(x["date"], y["date"]))

	# return str(entradas_list)

def main():
	entradas = get_entradas_list()

	process(entradas)
	
	return 0

if __name__ == '__main__':
	main()