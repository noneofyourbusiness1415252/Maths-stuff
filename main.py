# Go to README.md for guidance and information.
start=''
from Functions import *
import random
import os
global PrimeorCompositeNumber
global PrimeorCompositeRange
global SquareorCubeNumber
global SquareorCubeRange
global PrimeQuiz
global SquareorCubeQuiz
def PrimeorCompositeNumber():
  number = input('Enter a number.')
  print(number, PrimeorComposite(int(number)))
  SwitchMode()
def PrimeorCompositeRange():
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
def SquareorCubeNumber():
    number = int(input('Enter a number to find whether it is squared or cubed!\n'))
    print(number, SquareorCube(number))
    SwitchMode()
def SquareorCubeRange():
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
def PrimeQuiz():
  score = 0
  with open('UserAccounts/'+nickname+'/PrimeLevel.md') as PLfile:
      readPL = PLfile.read()
  if readPL =='':
      primelevel=1
      highestPL=1
  else:
      highestPL=int(readPL)
      PLs=list(range(1,int(highestPL)+1))
      choosePL=int(input('Type a level from 1 to '+str(highestPL)+'\n'))
      while PLs.count(choosePL)==0:
          choosePL=int(input('Invalid level, please try again\n'))
      primelevel=choosePL
  for a in range(10):
      primes=0
      composites=0
      randnum=()
      while randnum==():
          if primelevel == 1:
            primeorcomposite=random.randint(1,3)
            if primeorcomposite==3:
              for l in range(1,10):
                  if PrimeorComposite(l)=='is a prime number.':
                      rand=random.randint
                      if rand==4:
                          randnum=l
                  elif l%2 > 0 or l==2:
                      rand=random.randint(1,6)
                      if rand==6:
                          randnum=l
          else:
              for l in range((primelevel-1)**2*10+1,primelevel**2*10):
                  if PrimeorComposite(l)=='is a prime number.':
                      primes=primes+1
                  else:
                      composites=composites=composites+1
              for l in range((primelevel-1)**2*10+1,primelevel**2*10):
                  if PrimeorComposite(l)=='is a prime number':
                      rand=random.randint(1,primes)
                      if rand==primes:
                          randnum=l
                  elif l%2 > 0 or l == 2:
                      rand=random.randint(1,composites)
                      if rand==composites:
                          randnum=l
      text = 'Is ', str(randnum), ' a prime number?\n'
      answer = input(''.join(text))
      if PrimeorComposite(randnum) == 'is a prime number.':
          correct = 'yes'
      else:
          correct = 'no'
      if answer.lower()==correct:
          score=score+1
          print('Well done!')
      else:
          print('Oops! Correct answer is: '+correct)
  if score > 9 and primelevel==highestPL:
    highestPL = highestPL + 1
    primelevelup = 'Level up! You are now on level ', str(highestPL), '! Good work! You will now get harder questions!'
    print(''.join(primelevelup))
    with open('UserAccounts/'+nickname+'/PrimeLevel.md','w') as PLfile:
        PLfile.write(str(highestPL))
  SwitchMode()
def SquareorCubeQuiz():
    SOCLs=0
    score=0
    nonpowers=()
    powers=()
    with open('UserAccounts/'+nickname+'/SquareOrCubeLevel.md') as SOCLfile:
        readSOCL = SOCLfile.read()
        if readSOCL =='':
            squareorcubelevel=1
            highestSOCL=1
        else:
            highestSOCL=int(readSOCL)
            SOCLs=list(range(1,int(highestSOCL)+1))
            chooseSOCL=int(input('Choose a level from 1 to '+str(highestSOCL)+'\n'))
            while SOCLs.count(chooseSOCL)==0:
                chooseSOCL=int(input('Invalid level, please try again\n'))
            squareorcubelevel=chooseSOCL
    for a in range(10):
        powers=0
        nonpowers=0
        randnum=()
        while randnum==():
            if squareorcubelevel == 1:
                powerornonpower=random.randint(1,3)
                if powerornonpower==3:
                  for l in range(10):
                    if SquareorCube(l)=='is a prime number.':
                      rand=random.randint(1,4)
                      if rand==4:
                        randnum=l
                    else:
                        rand=random.randint(1,6)
                        if rand==6:
                            randnum=l
            else:
                for l in range((squareorcubelevel-1)**2*10+1,squareorcubelevel**2*10):
                  if SquareorCube(l)=='is not a square or cube number.':
                      nonpowers=nonpowers+1
                  else:
                      powers=powers+1
                for l in range((squareorcubelevel-1)**2*10+1,squareorcubelevel**2*10):
                      if SquareorCube(l)=='is not a square or cube number.':
                          rand=random.randint(1,nonpowers)
                          if rand==nonpowers:
                              randnum=l
                      else:
                          rand=random.randint(1,powers)
                          if rand==powers:
                              randnum=l
        text = 'Is '+ str(randnum)+ " a square number or cube number? Type 'both', 'square', 'cube' or 'no' accordingly. \n"
        answer = input(''.join(text))
        if SquareorCube(randnum) == 'is a power of 6, so it is both a square number and a cube number.':
            correct='both'
        elif SquareorCube(randnum) == 'is a square number.':
            correct='square'
        elif SquareorCube(randnum) == 'is a cube number.':
            correct='cube'
        else:
            correct='no'
        if answer.lower()==correct:
            print('Well done!')
            score=score+1
        else:
            print('Oops! The correct answer is:'+correct+'.')
    if score > 9 and squareorcubelevel==highestSOCL:
        highestSOCL=highestSOCL+1
        SOCLup = 'Level up! You are now on level ' + str(highestSOCL) + '. Good job!'
        print(''.join(SOCLup))
        with open('UserAccounts/'+nickname+'/SquareOrCubeLevel.md','w') as SOCLfile:
            SOCLfile.write(str(highestSOCL))
    SwitchMode()
nickname =input('Hello! Enter a nickname to save progress.\nIf you have used this tool before, enter the nickname you used last.\n')
if not os.path.exists('UserAccounts/'+nickname):
    os.mkdir('UserAccounts/'+nickname)
SOCLfile = open('UserAccounts/'+nickname+'/SquareOrCubeLevel.md','a+')
SOCLfile.close()
PLfile=open('UserAccounts/'+nickname+'/PrimeLevel.md','a+')
PLfile.close()
global SwitchMode
def SwitchMode():
  global start
  if start =='':
    start = input('Hello, '+nickname+'. This is a tool to find more about numbers. What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a quiz about squares and cubes.\nPlease go to code, then go to README.md for guidance and information.\n Please report any bugs or feedback in the comments below, or on\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff/issues\n')
  else:
    switch = input('Do you want to switch modes?\n')
    if switch.upper()=='YES':
      start=input('What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a quiz about squares and cubes.\n')
  if start=='1':
    PrimeorCompositeNumber()
  elif start=='2':
    PrimeorCompositeRange()
  elif start=='3':
    SquareorCubeNumber()
  elif start=='4':
    SquareorCubeRange()
  elif start=='5':
    PrimeQuiz()
  elif start=='6':
    SquareorCubeQuiz()
  else:
    start=input('Invalid option. Please type a number from 1 to 6 to choose a mode.')
SwitchMode()





