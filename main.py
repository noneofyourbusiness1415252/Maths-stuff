#!/usr/bin/env python
# Click 'Markdown' for guidance and information.
global SwitchMode
start = ""
from random import randint, uniform, choice, randrange
import os
from sys import stdout, float_info
import signal

from time import time

global score
from termcolor import cprint
from replit import db


def print_linenum(signum, frame):
	"""Press Ctrl+C at any time to print the current line"""
	print("\nCurrently at line", frame.f_lineno)


signal.signal(signal.SIGINT, print_linenum)
from time import sleep


def Prime(n):
	"""Returns whether or not n is prime. Example:\n `Prime(5)` returns `True`"""
	if n == 2 or n == 3:
		return True
	if n < 2 or n % 2 == 0:
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	r = int(n ** 0.5)
	f = 5
	while f <= r:
		if n % f == 0:
			return False
		if n % (f + 2) == 0:
			return False
		f += 6
	return True


def Power(n, p):
	"""Returns whether or not n is a pth power. Example: `Power(8,3)` returns `True`"""
	if p % 2 == 1:
		p = abs(p)
	else:
		if abs(n) != n:
			return False
	return round(abs(n) ** (1 / p)) ** p == abs(n)


def SquareorCube(n):
	"""Returns whether or not a number is square or cube, or both. Example: SquareorCube(64) returns `both`."""
	if Power(n, 2) and Power(n, 3):
		return "both"
	elif Power(n, 2):
		return "square"
	elif Power(n, 3):
		return "cube"
	else:
		return "neither"


def typewriter(t=""):
	"""Prints text as if typed on a typewriter, with options for colours and speed. Example: `typewriter('Some strong stringy strings')`"""
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


def intput(text, mode=int):
	"""Allows to accept integer input without worrying about the user typing something that is not an integer, which would return an error. Used just like input(). Example:\n `intput('Enter an integer.')`."""
	try:
		typewriter(text)
	except:
		print(text)
	while True:
		try:
			if mode == str:
				n = spell.correction(str(input()))
			else:
				n = mode(eval(input()))
		except EOFError:
			leave = intput("Are you sure you want to leave?\n")
			if leave.lower() != "y" and leave.lower() != "yes":
				print("Exiting...")
				exit()
		except:
			if mode == int:
				typewriter(f"Error: Please input an integer (whole number): ")
			else:
				typewriter(f"Error: Please type a number: ")
		else:
			return n


from spellchecker import SpellChecker

spell = SpellChecker()


def PrimeorCompositeNumber():
	"""Asks the user to input a number, and tells them whether or not it is prime."""
	number = intput("Enter a number: ")
	if Prime(number):
		typewriter(f"{number} is prime.\n")
	else:
		typewriter(f"{number} is composite.\n")
	SwitchMode()


def SquareorCubeNumber():
	"""Asks user to input 2 numbers, m and n, then informs the user whether or not m is an nth power."""
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
	"""Asks the user to input x and y, then returns the amount and list of primes/powers between x and y."""
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
		"The square numbers between " + str(num1) + "  and " + str(num2) + " are: "
	)
	l = num1
	while l != (num2 + 1):
		if primeorpower(l) == a:
			squares += 1
			squarenums = squarenums + str(l) + ", "
			cubeorprimenums += str(l) + ", "
			cubesorprimes += 1
			amount += 1
	if primeorpower == SquareorCube:
		l = num1
		while l != (num2 + 1):
			if primeorpower(l) == "cube":
				cubesorprimes += 1
				cubeorprimenums += str(l) + ", "
		l = num1
		while l != (num2 + 1):
			if primeorpower(l) == "square":
				squares = squares + 1
				squarenums += str(l) + ", "
	str1 = str(num1)
	str2 = str(num2)
	if primeorpower == Prime:
		if amount == 1:
			typewriter(f"There is 1 prime number between {str1}, and {str2}.\n")
		else:
			typewriter(f"There are {amount} prime numbers between {str1} and {str2}.\n")
		typewriter(f"{cubeorprimenums.replace('cube','prime')}\n")
	else:
		typewriter(
			f"There are {str(cubesorprimes)} cube numbers, and {str(squares)} square"
			f" numbers between {str1}  and {str2}.\n{squarenums}.\n{cubeorprimenums}."
		)

	SwitchMode()


def Quiz(primeorpower):
	"""A quiz that tests the user on their primes, squares and cubes using randomly generated questions with infinite levels. https://github.com/noneofyourbusiness1415252/Maths-stuff#how-questions-are-picked"""
	score = 0
	if primeorpower == Prime:
		a = False
		correct_a = "no"
		b = True
		c = a
		correct_b = "yes"
		correct_c = correct_a
		prompt = "Is __  a prime number? Type 'yes' or 'no'. \n"
		level_type = "PrimeLevel"
	else:
		a = "square"
		b = "cube"
		c = "neither"
		correct_a, correct_b, correct_c = a, b, c
		prompt = (
			"Is __ a square number or cube number? Type 'both', 'square', 'cube' or"
			" 'neither' accordingly. \n"
		)
		level_type = "SquareorCubeLevel"
	difficulty = intput(
		"How hard do you want the quiz to be? Type any number. A higher number = higher"
		" difficulty."
	)
	i = 0
	while True:
		start_range = round(i * difficulty ** 1.5)
		end_range = round((i + 1) * difficulty ** 1.5)
		powers = False
		n = start_range
		while n != end_range:
			if primeorpower(n) != c:
				if not powers:
					powers = []
				powers.append(n)
			n += 1
		Range = round(end_range - start_range)
		if powers and randint(1, Range) != Range:
			randnum = choice(powers)
		else:
			randnum = randint(start_range, end_range)
		if primeorpower(randnum) == "both":
			correct = "both"
		elif primeorpower(randnum) == a:
			correct = correct_a
		elif primeorpower(randnum) == b:
			correct = correct_b
		else:
			correct = correct_c
		start_time = time()
		answer = intput(prompt.replace("__", str(randnum)), str)
		end_time = time()
		if answer.lower() == correct:
			typewriter("Well done!")
			score += round(round((end_time - start_time) * randnum ** 0.75, 1) * 10)
			print(f"\nscore: {score}")
		else:
			try:
				if db[f"{owner}.{level_type}"] < score:
					print("High Score!")
					db[f"{owner}.{level_type}"] = score
			except:
				db[f"{owner}.{level_type}"] = score
			print(f"Game Over! Your score is: {score}")
			break
		i += 1
	SwitchMode()


def typewriterSet():
	"""Tool to change speed of typewriter effects."""
	write = input("Do you want to turn on typewriter effects?")
	if write.lower() == "yes":
		speed = intput(
			"Type a number to change speed of typewriter effect.\nNote that a lower"
			" amount means a higher speed, because it is measured	in average"
			" seconds delay between each letter.\nPress code, or go"
			" to\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff#readme\nfor"
			" more information.\n",
			float,
		)
		happy = intput(
			"This is how fast the effect will be. Are you happy with your changes?\n",
			str,
		)
		while happy.lower() == "no":
			speed = intput("Type a number to change speed.\n", float)
			typewriter(
				"This is how fast the effect will be. Are you happy with you changes?"
			)

	try:
		speed = db[f"{owner}.typespeed"]
	except:
		speed = float_info.min
		db[f"{owner}.typespeed"] = speed


def ColourSet():
	"""Tool to configure the (multi)coloured text"""
	coloured = intput("Do you want to turn on (multi)coloured text?", str)
	happy = "no"
	if coloured.lower() == "yes" or coloured.lower() == "y":
		while happy != "yes" and happy != "y":
			colours = []
			while not "done" in colours and not "all" in colours:
				c = intput(
					"Enter any colour to add to the multicoloured text. Choose from:"
					" red, green, yellow, blue, magenta, cyan or white. Type"
					' "all" to use all available colours. If you type a colour multiple'
					" times, it will appear more often than any other colours. Type"
					' "done" when finished to preview your configuration.',
					str,
				)
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
			happy = intput(
				"This is a preview of your configuration. Are you happy with your"
				" changes?",
				str,
			)

	else:
		db[f"{owner}.colours"] = "white"


owner = os.environ["REPL_OWNER"]
try:
	nickname = db[f"{owner}.nickname"]
except:
	nickname = intput(
		"Optional: Enter a nickname.\nLeave blank to keep your replit username"
		f" ({owner}) as your nickname\nnickname> ",
		str,
	)
	if nickname == "":
		nickname = owner
	db[f"{owner}.nickname"] = nickname
try:
	speed = db[f"{owner}.typespeed"]
except:
	typewriterSet()
try:
	colours = db[f"{owner}.colours"]
except:
	ColourSet()

start = (
	f"Hello, {nickname}! This is a tool to find more about numbers. What do you"
	" want to do? Type in a number to go to one of these modes: \nType 1 to"
	" find out if a number is prime or composite. \nType 2 to find out how"
	" many Prime numbers are between 2 numbers\nType 3 to find out if X is a"
	" Yth power, i.e. if a number is squared, cubed, tesseractic etc.\nType 4"
	" to find out how many squares and cubes there are between 2"
	" numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a"
	" quiz about squares and cubes.\nType 7 to turn on/change typewriter"
	" effect.\nType 8 to turn on/change colored text.\nPlease click code, or"
	" visit\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff#readme\nfor"
	" more information.\nPlease report any bugs or feedback in the comments"
	" below, or"
	" on\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff/issues\n"
)
original_start = start


def SwitchMode():
	"""Used to switch modes in the maths stuff program."""
	global start
	if start == original_start:
		start = intput(start)
	else:
		switch = intput("Do you want to switch modes?\n", str)
		if switch.upper() == "YES":
			start = intput(original_start)

	def choose(start):
		if start == 1:
			PrimeorCompositeNumber()
		elif start == 2:
			PowerandPrimeRange(Prime)
		elif start == 3:
			SquareorCubeNumber()
		elif start == 4:
			PowerandPrimeRange(SquareorCube)
		elif start == 5:
			Quiz(Prime)
		elif start == 6:
			Quiz(SquareorCube)
		elif start == 7:
			typewriterSet()
		elif start == 8:
			ColourSet()
		else:
			return "e"

	while choose(start) == "e":
		start = intput("Oops! Please type a number from 1 to 9 to choose a mode.")
		choose(start)


SwitchMode()
