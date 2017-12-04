#Advent of Code 2017
#Day 1 Challenge
#http://adventofcode.com/2017/day/1
#Author: Sam Clark


import sys

def captcha_solver ( captcha ) :
	result = 0	
	list(captcha)
	prev_char = captcha[-1]
	
	for digit in captcha :
		if digit == prev_char :
			result += int(digit)
		prev_char = digit
	return result

print("Advent of Code 2017")
print("Day 1 - http://adventofcode.com/2017/day/1")
print("Sam Clark")

selection = '\0'

while (selection != 'Q' and selection != 'q') :
	print("Solution: ", captcha_solver(input("\nEnter your captcha: ")))
	selection = input("\nPress q to quit. Any other key to continue.")
	
sys.exit()