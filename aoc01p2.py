#Advent of Code 2017
#Day 1 Challenge, part 2
#http://adventofcode.com/2017/day/1
#Author: Sam Clark


import sys
from itertools import islice

print("Advent of Code 2017")
print("Day 1, part 2 - http://adventofcode.com/2017/day/1")
print("Sam Clark")

def captcha_solver ( captcha ) :
	result = 0	
	half = len(captcha)//2
	list(captcha)
	
	for i, digit in enumerate(islice(captcha,0,half)) :
		if digit == captcha[i + half] :
			result += 2 * int(digit)
	return result


selection = '\0'

while (selection != 'Q' and selection != 'q') :
	print("Solution: ", captcha_solver(input("\nEnter your captcha: ")))
	selection = input("\nPress q to quit. Any other key to continue.")
	
sys.exit()