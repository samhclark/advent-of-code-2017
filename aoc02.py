#Advent of Code 2017
#Day 2 Challenge
#http://adventofcode.com/2017/day/2
#Author: Sam Clark

import sys
import csv

print("Advent of Code 2017")
print("Day 2 - http://adventofcode.com/2017/day/2")
print("Sam Clark")

def checksum ( spreadsheet ) :
	diffs = []
	for row in spreadsheet : 
		diffs.append(int(max(row))-int(min(row)))
	return sum(diffs)


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