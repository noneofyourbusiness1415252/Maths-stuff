# Go to README.md for guidance and information.
global SwitchMode
start = ""
from Functions import *
from random import randint, uniform, choice
import os

global PrimeorCompositeNumber
global PrimeorCompositeRange
global SquareorCubeNumber
global SquareorCubeRange
global Quiz
global typewriter
global chooseTP
import signal
from math import *

global score
from termcolor import cprint
from replit import db


def print_linenum(signum, frame):
	print("\nCurrently at line", frame.f_lineno)


signal.signal(signal.SIGINT, print_linenum)
from time import sleep
import sys
from spellchecker import SpellChecker
spell = SpellChecker()

def PrimeorCompositeNumber():
	typewriter("Enter a number.\n")
	number = int(input())
	typewriter(str(number) + PrimeorComposite(int(number)))
	SwitchMode()


def SquareorCubeNumber():
	typewriter("Enter a number to find whether it is square, cube, tesseractic etc.\n")
	number = int(input())
	typewriter(
		f"Enter the power.\nFor example, type 2 if you want to check if {number} is a"
		f" square number, 3 if you want to check if {number} is a cube number, or 4 if"
		f" you want to check if {number} is a tesseractic number.\n"
	)
	power = int(input())
	if Power(number, power):
		if power == 2:
			typewriter(f"Yes; {number} is a square number.")
		elif power == 3:
			typewriter(f"Yes; {number} is a cube number.")
		elif power == 4:
			typewriter(f"Yes;{number} is a tesseractic number.")
		else:
			typewriter(f"Yes; {number} is a {power}th power.")
	else:
		print(f"No.")
		if power == 2:
			typewriter(f"No; {number} is not a square number.")
		elif power == 3:
			typewriter(f"No; {number} is not a cube number.")
		elif power == 4:
			typewriter(f"No;{number} is not a tesseractic number.")
		else:
			typewriter(f"No; {number} is not a {power}th power.")
	SwitchMode()


def PowerandPrimeRange(primeorpower):
	if primeorpower == Prime:
		a = "is a composite number."
		correct_a = "no"
		c = a
		correct_c = correct_a
		b = "is a prime number."
		prompt = 'Is __ a prime number? Type "yes" or "no".'
	else:
		a = "is a square number."
		correct_a = "square"
		b = "is a cube number."
		correct_b = "cube"
		c = "is not a square or cube number."
		correct_c = "neither"
		prompt = (
			'Is __ a square number, a cube number or both? Type "square", "cube",'
			' "both" or "neither" accordingly.'
		)
	typewriter("Enter the first number\n")
	num1 = int(input())
	typewriter("Enter the second number.\n")
	num2 = int(input())
	cubesorprimes = 0
	squares = 0
	cubeorprimenums = (
		"The cube numbers between " + str(num1) + " and " + str(num2) + " are: "
	)
	squarenums = (
		"The square numbers between " + str(num1) + " and " + str(num2) + " are: "
	)
	for l in range(num1, num2 + 1):
		if (
			primeorpower(l)
			== "is a power of 6, so it is both a square number and a cube number."
		):
			squares += 1
			squarenums = squarenums + str(l) + ", "
			cubeorprimenums = cubeorprimenums + str(l) + ", "
	if primeorpower == SquareorCube:
		for l in range(num1, num2 + 1):
			if primeorpower(l) == "is a cube number.":
				cubesorprimes += 1
				cubeorprimenums = cubeorprimenums + str(l) + ", "
		for l in range(num1, num2 + 1):
			if primeorpower(l) == "is a square number.":
				squares = squares + 1
				squarenums = squarenums + str(l) + ", "
	str1 = str(num1)
	str2 = str(num2)
	if primeorpower == PrimeorComposite:
		if amount == 1:
			typewriter(f"There is 1 prime number between {str1}, and {str2}")
		else:
			typewriter(
				"there are" + amount, "prime numbers between" + num1, "and", num2
			)
		typewriter(
			f"These are the prime numbers between {str1} and {str2}: {cubeorprimenums}"
		)
	else:
		typewriter(
			f"There are {str(cubesorprimes)} cube numbers, and {str(squares)} square"
			f" numbers between {str1}  and {str2}.\nThese are the square numbers"
			f" between {str1} and {str2}: {squarenums}.\nThese are the cube numbers"
			f" between {str1} and {str2}: {cubeorprimenums}."
		)

	SwitchMode()


def Quiz(primeorpower):
	if primeorpower == Prime:
		a = False
		correct_a = 'no'
		b = True
		c = a
		correct_b = "yes"
		level_type = "PL"
		prompt = f"Is __  a prime number? Type 'yes' or 'no'. \n"
	else:
		a = "square"
		b = "cube"
		c = "neither"
		correct_a, correct_b, correct_c = a, b, c
		level_type = "SOCL"
		prompt = (
			"Is __ a square number or cube number? Type 'both', 'square', 'cube' or"
			" 'neither' accordingly. \n"
		)
	score = 0
	try:
		level = db[f"{owner}.{level_type}"]
	except:
		level = 1
	highestLevel = int(level)
	typewriter("Choose a level from 1 to " + str(highestLevel) + "\nlevel> ")
	chooseLevel = int(input())
	while highestLevel < chooseLevel:
		typewriter("Invalid level, please try again.\nlevel> ")
		chooseLevel = input()
	level = chooseLevel
	minimum = level ** 2 * 5
	possible_questions = (level + 1) ** 2 * 5 - minimum
	range_amount = possible_questions / 5
	total_powers = None
	i = 0
	while i < 5:
		powers = False
		current_range = minimum + range_amount * i
		for n in range(round(current_range), round(current_range + range_amount)):
			if primeorpower(n) != c:
				if not powers:
					powers = []
				powers.append(n)
		if powers:
			randnum = choice(powers)
		else:
			randnum = randint(current_range, current_range + range_amount)
		typewriter(prompt.replace("__", str(randnum)))
		answer = input("")
		if Power(randnum, 2) and Power(randnum, 3):
			correct = "both"
		elif primeorpower(randnum) == a:
			correct = correct_a
		elif primeorpower(randnum) == b:
			correct = correct_b
		else:
			correct = correct_c
		if spell.correction(answer.lower()) == correct:
			typewriter("Well done!")
			score = score + 1
		else:
			typewriter("Oops! The correct answer is:" + correct + ".")
		i += 1
	if score >= 5 and level == highestLevel:
		highestLevel += 1
		typewriter(f"Level up! You are now on level {str(highestLevel)}. Good job!")
	db[f"{owner}.{level_type}"] = highestLevel
	SwitchMode()


owner = os.environ["REPL_OWNER"]
try:
	nickname = db[f"{owner}.nickname"]
except:
	nickname = input(
		"Optional: Enter a nickname.\nLeave blank to keep your replit username"
		f" ({owner}) as your nickname\nnickname> "
	)
	if nickname == "":
		nickname = owner
	db[f"{owner}.nickname"] = nickname
if not os.path.exists("UserAccounts/" + nickname):
	os.mkdir("UserAccounts/" + nickname)
try:
	speed = db[f"{owner}.typespeed"]
except:
	write = input("Do you want to turn on typewriter effects?")
	if write.lower() == "yes":
		speed = float(
			input(
				"Type a number to change speed of typewriter effect.\nNote that a lower"
				" amount means a higher speed, because it is measured	in average"
				" seconds delay between each letter.\nPress code, or go"
				" to\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff#readme\nfor"
				" more information.\n"
			)
		)
		typewriter(
			"This is how fast the effect will be. Are you happy with your changes?\n"
		)
		happy = input()
		while happy.lower() == "no":
			typewriter("Type a number to change speed.\n")
			speed = float(input())
			typewriter(
				"This is how fast the effect will be. Are you happy with your"
				" changes?\n"
			)
			happy = input()
	else:
		speed = 0
	db[f"{owner}.typespeed"] = speed


def typewriter(t):
	for x in t:
		cprint(x, end="")
		sys.stdout.flush()
		sleep(uniform(0, db[f"{owner}.typespeed"] * 2))


def SwitchMode():
	global start
	if start == "":
		typewriter(
			"Hello, "
			+ nickname
			+ ". This is a tool to find more about numbers. What do you want to do?"
			" Type in a number to go to one of these modes: \nType 1 to find out if a"
			" number is prime or composite. \nType 2 to find out how many Prime numbers"
			" are between 2 numbers\nType 3 to find out if a X is a Yth power, i.e. if"
			" a number is squared, cubed, tesseractic etc.\nType 4 to find out how many"
			" squares and cubes there are between 2 numbers.\nType 5 for a quiz about"
			" primes and composites.\nType 6 for a quiz about squares and cubes.\nType"
			" 7 to turn on/change typewriter effect!\nPlease click code, or"
			" visit\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff#readme\nfor"
			" more information.\nPlease report any bugs or feedback in the comments"
			" below, or"
			" on\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff/issues\n"
		)
		start = input()
	else:
		typewriter("Do you want to switch modes?\n")
		switch = input()
		if switch.upper() == "YES":
			typewriter(
				"What do you want to do? Type in a number to go to one of these modes:"
				" \nType 1 to find out if a number is prime or composite. \nType 2 to"
				" find out how many Prime numbers are between 2 numbers\nType 3 to find"
				" out if a number is squared or cubed.\nType 4 to find out how many"
				" squares and cubes there are between 2 numbers.\nType 5 for a quiz"
				" about primes and composites.\nType 6 for a quiz about squares and"
				" cubes.\nType 7 to change typewriter effect speed!\n"
			)
			start = input()
	if start == "1":
		PrimeorCompositeNumber()
	elif start == "2":
		PowerandPrimeRange(PrimeorComposite)
	elif start == "3":
		SquareorCubeNumber()
	elif start == "4":
		PowerandPrimeRange(SquareorCube)
	elif start == "5":
		Quiz(PrimeorComposite)
	elif start == "6":
		Quiz(SquareorCube)
	elif start == "7":
		typewriter("Do you want to turn on typewriter effects?\n")
		write = input()
		if write.lower() == "yes":
			typewriter(
				"Type a number to change speed of typewriter effect.\nNote that a lower"
				" amount means a higher speed, because it is measured in average"
				" seconds delay between each letter.\n"
			)
			speed = float(input())
			print("Enter a colour for your effect. Choose from: ")
			cprint("Red", "red")
			cprint("Grey", "grey")
			cprint("Green", "green")
			cprint("Yellow", "yellow")
			cprint("Blue", "blue")
			cprint("Magenta", "magenta")
			cprint("Cyan", "cyan")
			cprint("White", "white")
			cprint("C", "grey", end="")
			cprint("o", "red", end="")
			cprint("l", "green", end="")
			cprint("o", "yellow", end="")
			cprint("r ", "blue", end="")
			cprint("f", "magenta", end="")
			cprint("u", "cyan", end="")
			cprint("l", "white", end="")
			colour = input()
			typewriter(
				"This is how fast the effect will be. Are you happy with your"
				" changes?\n"
			)
			happy = input()
			while happy.lower() != "yes":
				db[f"{owner}.typespeed"] = float(
					input("Type a number to change speed.\n")
				)
				typewriter(
					"This is how fast the effect will be. Are you happy with your"
					" changes?\n"
				)
				print(speed)
				happy = input()
		SwitchMode()
	else:
		start = input(
			"Invalid option. Please type a number from 1 to 7 to choose a mode.\n"
		)


SwitchMode()
