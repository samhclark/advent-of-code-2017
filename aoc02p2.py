#Advent of Code 2017
#Day 2 Challenge, Part 2
#http://adventofcode.com/2017/day/2
#Author: Sam Clark

import sys
import csv

print("Advent of Code 2017")
print("Day 2, Part 2 - http://adventofcode.com/2017/day/2")
print("Sam Clark")

def checksum ( spreadsheet ) :
	quotients = []
	checked = []
	for row in spreadsheet : 
		for i in row :
			for j in checked :
				if j % i == 0 :
					quotients.append(j/i)
					break
				if i % j == 0 :
					quotients.append(i/j)
					break
			checked.append(i)
		checked.clear()
	return sum(quotients)


selection = '\0'

while (selection != 'Q' and selection != 'q') :
	file_name = input("\nEnter your spreadsheet filename (csv): ")
	with open(file_name, 'rU') as f :
		reader = csv.reader(f)
		data = list(list(rec) for rec in csv.reader(f, delimiter='\t'))

	for i in range(len(data)) :
		for j in range(len(data[i])) :
			data[i][j] = int(data[i][j])

	print("Solution: ", checksum(data))

	selection = input("\nPress q to quit. Any other key to continue.")
	
sys.exit()