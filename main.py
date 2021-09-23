# Click 'Markdown' for guidance and information.
global SwitchMode
start = ""
from Functions import *
from random import randint, uniform, choice, randrange
import os
from sys import stdout, float_info, getsizeof

global PrimeorCompositeNumber
global PrimeorCompositeRange
global SquareorCubeNumber
global SquareorCubeRange
global Quiz
global typewriter
global chooseTP
global colours
import signal
from math import *

global score
from termcolor import cprint
from replit import db


def print_linenum(signum, frame):
	print("\nCurrently at line", frame.f_lineno)


signal.signal(signal.SIGINT, print_linenum)
from time import sleep


def typewriter(t):
	try:
		speed = db[f"{owner}.typespeed"]
	except:
		speed = float_info.min
	try:
		colours = db[f"{owner}.colours"]
	except:
		colours = ["white"]
	for x in t:
		if len(colours) == 1:
			rc = 0
		else:
			rc = randrange(len(colours))
		cprint(x, colours[rc], end="")
		stdout.flush()
		sleep(uniform(0, speed * 2))


def intput(text):
	typewriter(text)
	while True:
		try:
			n = int(input())
		except:
			typewriter("Please input an integer (whole number): ")
		else:
			return n


try:
	from spellchecker import SpellChecker
except:
	os.system("pip install pyspellchecker")
	from spellchecker import SpellChecker
spell = SpellChecker()


def PrimeorCompositeNumber():
	number = intput("Enter a number: ")
	if Prime(number):
		typewriter(f"{number} is prime.\n")
	else:
		typewriter(f"{number} is composite.\n")
	SwitchMode()


def SquareorCubeNumber():
	number = intput(
		"Enter a number to find whether it is square, cube, tesseractic etc.: "
	)
	power = intput(
		f"Enter the power.\nFor example, type 2 if you want to check if {number} is a"
		f" square number, 3 if you want to check if {number} is a cube number, or 4 if"
		f" you want to check if {number} is a tesseractic number: "
	)
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
	amount = 0
	if primeorpower == Prime:
		a = True
	else:
		a = "both"
	num1 = intput("Enter the first number: ")
	num2 = intput("Enter the second number: ")
	cubesorprimes = 0
	squares = 0
	cubeorprimenums = (
		"The cube numbers between " + str(num1) + " and " + str(num2) + " are: "
	)
	squarenums = (
		"The square numbers between " + str(num1) + " and " + str(num2) + " are: "
	)
	for l in range(num1, num2 + 1):
		if primeorpower(l) == a:
			squares += 1
			squarenums = squarenums + str(l) + ", "
			cubeorprimenums = cubeorprimenums + str(l) + ", "
			cubesorprimes += 1
			amount += 1
	if primeorpower == SquareorCube:
		for l in range(num1, num2 + 1):
			if primeorpower(l) == "cube":
				cubesorprimes += 1
				cubeorprimenums = cubeorprimenums + str(l) + ", "
		for l in range(num1, num2 + 1):
			if primeorpower(l) == "square":
				squares = squares + 1
				squarenums = squarenums + str(l) + ", "
	str1 = str(num1)
	str2 = str(num2)
	if primeorpower == Prime:
		if amount == 1:
			typewriter(f"There is 1 prime number between {str1}, and {str2}.\n")
		else:
			typewriter(f"There are {amount} prime numbers between {str1} and {str2}.\n")
		typewriter(
			f"These are the prime numbers between {str1} and {str2}:"
			f" {cubeorprimenums}.\n"
		)
	else:
		typewriter(
			f"There are {str(cubesorprimes)} cube numbers, and {str(squares)} square"
			f" numbers between {str1}  and {str2}.\n{squarenums}.\n{cubeorprimenums}."
		)

	SwitchMode()


def Quiz(primeorpower):
	if primeorpower == Prime:
		a = False
		correct_a = "no"
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
	chooseLevel = intput("Choose a level from 1 to " + str(highestLevel) + "\nlevel> ")
	while highestLevel < chooseLevel:
		chooseLevel = intput("Invalid level, please try again.\nlevel> ")
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
	if owner == "five-nine":
		nickname = input(
			"Enter a nickname to save progress. If you have already used this before,"
			" use your previous nickname: "
		)
		while len(nickname) > 32:
			typewriter(
				"Nickname too long! Must be between 8 and 32 characters, and consist of"
				" only ASCII (English letters, numbers and symbols. : "
			)
			nickname = input()
		try:
			password = db[f"{nickname}.password"]
		except:
			password = input(
				"Enter a password. Sign into replit to prevent having to type a"
				" nickname and password here."
			)
			while 8 < len(password) < 32 or not password.isascii():
				typewriter(
					"Password invalid. It must be between 8 and 32 characters, and only"
					" contain English symbols, letters and numbers."
				)
				password = input()
		db[f"{nickname}.password"] = password
	db[f"{owner}.nickname"] = nickname
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
				"This is how fast the effect will be. Are you happy with you changes?"
			)
	try:
		speed = db[f"{owner}.typespeed"]
	except:
		speed = float_info.min
		db[f"{owner}.typespeed"] = speed
try:
	colours = db[f"{owner}.colours"]
except:
	typewriter("Do you want to turn on (multi)coloured text?")
	coloured = input()
	happy = "no"
	if coloured.lower() == "yes" or coloured.lower() == "y":
		while spell.correction(happy) != "yes" and happy != "y":
			colours = []
			while not "done" in colours and not "all" in colours:
				typewriter(
					"Enter any colour to add to the multicoloured text. Choose from:"
					" red, green, yellow, blue, magenta, cyan or white. Type"
					' "all" to use all available colours. If you type a colour multiple'
					" times, it will appear more often than any other colours. Type"
					' "done" when finished to preview your configuration.'
				)
				c = input()
				colours.append(c)
			if "all" in colours:
				db[f"{owner}.colours"] = [
					"red",
					"green",
					"yellow",
					"blue",
					"magenta",
					"cyan",
					"white",
				]
			else:
				db[f"{owner}.colours"] = colours
			typewriter(
				"This is a preview of your configuration. Are you happy with your"
				" changes?"
			)
			happy = input()

	else:
		db[f"{owner}.colours"] = "white"


def SwitchMode():
	global start
	if start == "":
		typewriter(
			f"Hello, {nickname}! This is a tool to find more about numbers. What do you"
			" want to do? Type in a number to go to one of these modes: \nType 1 to"
			" find out if a number is prime or composite. \nType 2 to find out how"
			" many Prime numbers are between 2 numbers\nType 3 to find out if X is a"
			" Yth power, i.e. if a number is squared, cubed, tesseractic etc.\nType 4"
			" to find out how many squares and cubes there are between 2"
			" numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a"
			" quiz about squares and cubes.\nType 7 to turn on/change typewriter"
			" effect!\nPlease click code, or"
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
				" out if X is a Yth power, i.e. if a number is squared, cubed,"
				" tesseractic etc\nType 4 to find out how many squares and cubes there"
				" are between 2 numbers.\nType 5 for a quiz about primes and"
				" composites.\nType 6 for a quiz about squares and cubes.\nType 7 to"
				" change typewriter effect speed!\n"
			)
			start = input()
	if start == "1":
		PrimeorCompositeNumber()
	elif start == "2":
		PowerandPrimeRange(Prime)
	elif start == "3":
		SquareorCubeNumber()
	elif start == "4":
		PowerandPrimeRange(SquareorCube)
	elif start == "5":
		Quiz(Prime)
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
