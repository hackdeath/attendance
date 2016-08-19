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
	
def main():
    pass

if __name__ == '__main__':
	main()
