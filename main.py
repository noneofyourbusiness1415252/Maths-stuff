#Please do not use this program; it is still in development. Use the other one which isn't marked with DEV.
from Functions import *
import random
import os
squareorcubelevel = 1
primelevel = 1
nickname =input('Hello! Enter a nickname to save progress.\nIf you have used this tool before, enter the nickname you used last.\n')
if not os.path.exists('UserAccounts/'+nickname):
  os.mkdir('UserAccounts/'+nickname)
start = input('Hello, '+nickname+'. This is a tool to find more about numbers. What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a quiz about squares and cubes.\nPlease go to code, then go to README.md for guidance and information.\n')
while start == '1':
	number = input('Enter a number.')
	print(number, PrimeorComposite(int(number)))
	SwitchMode()
while start == '2':
	num1 = int(input('Enter the first number\n'))
	num2 = int(input('Enter the second number\n'))
	amount = 0
	primes = ('these are the prime numbers between' + str(num1) + ' and ' +
	          str(num2) + ': ')
	for l in range(num1, num2 + 1):
		if PrimeorComposite(l) == 'is a prime number.':
			amount = amount + 1
			primes = primes + str(l) + ', '
	if amount == 1:
		print('there is 1 prime number between', num1, 'and', num2)
	else:
		print('there are', amount, 'prime numbers between', num1, 'and', num2)
	Total = ''.join(primes)
	print(Total)
	SwitchMode()
while start == '3':
	number = int(
	    input('Enter a number to find whether it is squared or cubed!\n'))
	print(number, SquareorCube(number))
	SwitchMode()
while start == '4':
	num1 = int(input('Enter the first number\n'))
	num2 = int(input('Enter the second number.\n'))
	cubes = 0
	squares = 0
	cubenums = 'The cube numbers between ' + str(num1) + ' and ' + str(
	    num2) + ' are: '
	squarenums = 'The square numbers between ' + str(num1) + ' and ' + str(
	    num2) + ' are: '
	for l in range(num1, num2 + 1):
		if SquareorCube(
		    l
		) == 'is a power of 6, so it is both a square number and a cube number.':
			squares = squares + 1
			cubes = cubes + 1
			squarenums = squarenums + str(l) + ', '
			cubenums = cubenums + str(l) + ', '
	for l in range(num1, num2 + 1):
		if SquareorCube(l) == 'is a cube number.':
			cubes = cubes + 1
			cubenums = cubenums + str(l) + ', '
	for l in range(num1, num2 + 1):
		if SquareorCube(l) == 'is a square number.':
			squares = squares + 1
			squarenums = squarenums + str(l) + ', '
	total = ('There are ', str(cubes), ' cube numbers, and ', str(squares),
	         ' square numbers between ', str(num1), ' and ', str(num2), '.')
	print(''.join(total))
	totallist = cubenums + '\n' + squarenums
	print(''.join(totallist))
	SwitchMode()
while start == '5':
	score = 0
	for a in range(10):
		if primelevel == 1:
			rand = random.randint(1, 10)
		else:
			rand = random.randint(
			    primelevel**2 * 10 - (primelevel - 1)**2 * 10,
			    primelevel**2 * 10)
		text = 'Is ', str(rand), ' a prime number?\n'
		answer = input(''.join(text))
		if PrimeorComposite(rand) == 'is a prime number.':
			if answer.upper() == 'YES':
				print('Well done!')
				score = score + 1
			else:
				print('Oops. Incorrect answer!')
		else:
			if answer.upper() == 'NO':
				print('Well done!')
				score = score + 1
			else:
				print('Oops. Incorrect answer!')
	if score > 9:
		primelevel = primelevel + 1
		primelevelup = 'Level up! You are now on level ', str(
		    primelevel), '! Good work! You will now get harder questions!'
		print(''.join(primelevelup))
		SwitchMode()
while start == '6':
  with open('UserAccounts/'+nickname+'/SquareOrCubeLevel.txt','w+') as SOCL:
    squareorcubelevel = SOCL.read()
    if squareorcubelevel =='':
      squareorcubelevel=1
    else:
      squareorcubelevel=int(SOCL.read())
  score = 0
  powers =() 
  nonpowers=()
  if squareorcubelevel ==1:
    randnum = random.randint(1,10)
    nonpowers = [1,4,8,9]
    nonpowers = [2,3,5,6,7,10]
  else:
    for a in range((squareorcubelevel-1)**2*10+1,squareorcubelevel+1):
       if SquareorCube(a)=='is not a square or cube number.':
          nonpowers=[nonpowers, l]
       else:
         powers=[powers, l]        
  for a in range(10):
    powerornonpower=random.randint(1,3)
    powerornonpower = random.randint(1,3)
    if powerornonpower==1:
      randnum = random.choice(nonpowers)
    else:
      randnum=random.choice(nonpowers)
    text = 'Is '+ str(randnum)+ " a square number or cube number? Type 'both', 'square', 'cube' or 'no' accordingly. \n"
    answer = input(''.join(text))
    if SquareorCube(randnum) == 'is a power of 6, so it is both a square number and a cube number.':
      if answer.upper() == 'BOTH':
        print('Well done!!')
        score = score + 1
      else:
        print('Oops! Incorrect answer!')
    elif SquareorCube(randnum) == 'is a square number.':
      if answer.upper() == 'SQUARE':
        print('Well done!')
        score = score + 1
      else:
         print('Oops! Incorrect answer.')
    elif SquareorCube(randnum) == 'is a cube number.':
      if answer.upper() == 'CUBE':
        print('Well done!')
        score = score + 1
      else:
        print('Oops! Incorrect answer!')
    else:
      if answer.upper() == 'NO':
        print('Well done!')
        score = score + 1
      else:
      	print('Oops. Incorrect answer!')
  if score > 9:
    squareorcubelevel = squareorcubelevel + 1
    squarecubelevelup = 'Level up! You are now on level ' + str(
    squareorcubelevel) + '. Good job!'
    print(''.join(squarecubelevelup))
    SwitchMode()
    with open('UserAccounts/'+nickname+'/SquareOrCubeLevel.txt'+'w+') as save:
      save.write(squareorcubelevel)
while start=='5':
  bug=input('Please enter any bug you have encountered.')
  with open('Bugs/'+nickname+'.txt','w+') as bugfile:
    bugfile.write(bug)
  print('Thank you for reporting bugs! I appreciate your help,'+nickname+'!')


