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
global typewriter
global speed
global chooseTP
from time import sleep
import sys
def PrimeorCompositeNumber():
  typewriter('Enter a number.\n')
  number=int(input())
  print(number, PrimeorComposite(int(number)))
  SwitchMode()
def PrimeorCompositeRange():
    typewriter('Enter the first number\n')
    num1=int(input())
    typewriter('Enter the second number\n')
    num2=int(input())
    amount = 0
    primes = ('these are the prime numbers between' + str(num1) + ' and ' +
                      str(num2) + ': ')
    for l in range(num1, num2 + 1):
        if PrimeorComposite(l) == 'is a prime number.':
            amount = amount + 1
            primes = primes + str(l) + ', '
    if amount == 1:
        typewriter('there is 1 prime number between', num1, 'and', num2)
    else:
        typewriter('there are', amount, 'prime numbers between', num1, 'and', num2)
    Total = ''.join(primes)
    typewriter(Total)
    SwitchMode()
def SquareorCubeNumber():
    typewriter('Enter a number to find whether it is squared or cubed!\n')
    number=int(input())
    print(number, SquareorCube(number))
    SwitchMode()
def SquareorCubeRange():
  typewriter('Enter the first number\n')
  num1=int(input())
  typewriter('Enter the second number.\n')
  num2=int(input())
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
  total = ('There are ', str(cubes), ' cube numbers, and ', str(squares),' square numbers between ', str(num1), ' and ', str(num2), '.')
  typewriter(''.join(total))
  totallist = cubenums + '\n' + squarenums
  typewriter(''.join(totallist))
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
      typewriter('Type a level from 1 to '+str(highestPL)+'\n')
      choosePL=int(input())
      while PLs.count(choosePL)==0:
          typewriter('Invalid level, please try again\n')
          choosePL=input()
      primelevel=choosePL
  chosen=''
  for a in range(10):
      primes=0
      composites=0
      randnum=()
      while randnum==():
          if primelevel == 1:
            primeorcomposite=random.randint(1,3)
            if primeorcomposite==3:
              for l in range(1,10):
                if not chosen.__contains__(l):
                  if PrimeorComposite(l)=='is a prime number.':
                    rand=random.randint(1,4)
                    if rand==4:
                      chosen=chosen+str(l)
                      randnum=l
                  elif l%2 > 0 or l==2:
                    rand=random.randint(1,6)
                    if rand==6:
                      chosen=chosen+str(l)
                      randnum=l
          else:
            if not chosen.__contains__(l):
              for l in range((primelevel-1)**2*10+1,primelevel**2*10):
                if PrimeorComposite(l)=='is a prime number.':
                  primes=primes+1
                else:
                  composites=composites=composites+1
              for l in range((primelevel-1)**2*10+1,primelevel**2*10):
                if PrimeorComposite(l)=='is a prime number':
                  rand=random.randint(1,primes)
                  if rand==primes:
                    chosen=chosen+str(l)
                    randnum=l
                elif l%2 > 0 or l == 2:
                    rand=random.randint(1,composites)
                    if rand==composites:
                      chosen=chosen+str(l)
                      randnum=l
      text = 'Is ', str(randnum), ' a prime number?\n'
      typewriter(''.join(text))
      answer=input()
      if PrimeorComposite(randnum) == 'is a prime number.':
          correct = 'yes'
      else:
          correct = 'no'
      if answer.lower()==correct:
          score=score+1
          typewriter('Well done!')
      else:
          typewriter('Oops! Correct answer is: '+correct)
  if score > 9 and primelevel==highestPL:
    highestPL = highestPL + 1
    primelevelup = 'Level up! You are now on level ', str(highestPL), '! Good work! You will now get harder questions!'
    typewriter(''.join(primelevelup))
    with open('UserAccounts/'+nickname+'/PrimeLevel.md','w') as PLfile:
        PLfile.write(str(highestPL))
  SwitchMode()
def SquareorCubeQuiz():
    SOCLs=0
    score=0
    nonpowers=()
    powers=()
    chosen=()
    with open('UserAccounts/'+nickname+'/SquareOrCubeLevel.md') as SOCLfile:
        readSOCL = SOCLfile.read()
        if readSOCL =='':
            squareorcubelevel=1
            highestSOCL=1
        else:
            highestSOCL=int(readSOCL)
            SOCLs=list(range(1,int(highestSOCL)+1))
            typewriter('Choose a level from 1 to '+str(highestSOCL)+'\n')
            chooseSOCL=int(input())
            while SOCLs.count(chooseSOCL)==0:
                typewriter('Invalid level, please try again\n')
                chooseSOCL=input()
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
                if not chosen.__contains__(l):
                  if SquareorCube(l)=='is a prime number.':
                    rand=random.randint(1,4)
                    if rand==4:
                      chosen=chosen,l
                      randnum=l
                  else:
                    rand=random.randint(1,6)
                    if rand==6:
                      randnum=l
                      chosen=chosen,l
            else:
              for l in range((squareorcubelevel-1)**2*10+1,squareorcubelevel**2*10):
                if SquareorCube(l)=='is not a square or cube number.':
                  nonpowers=nonpowers+1
                else:
                  powers=powers+1
              for l in range((squareorcubelevel-1)**2*10+1,squareorcubelevel**2*10):
                if not chosen.__contains__(l):
                  if SquareorCube(l)=='is not a square or cube number.':
                    rand=random.randint(1,nonpowers)
                    if rand==nonpowers:
                      randnum=l
                      chosen=chosen,l
                    else:
                      rand=random.randint(1,powers)
                      if rand==powers:
                        randnum=l
                        chosen=chosen,l
        text = 'Is '+ str(randnum)+ " a square number or cube number? Type 'both', 'square', 'cube' or 'no' accordingly. \n"
        typewriter(text)
        answer = input()
        if SquareorCube(randnum) == 'is a power of 6, so it is both a square number and a cube number.':
            correct='both'
        elif SquareorCube(randnum) == 'is a square number.':
            correct='square'
        elif SquareorCube(randnum) == 'is a cube number.':
            correct='cube'
        else:
            correct='no'
        if answer.lower()==correct:
            typewriter('Well done!')
            score=score+1
        else:
            typewriter('Oops! The correct answer is:'+correct+'.')
    if score > 9 and squareorcubelevel==highestSOCL:
        highestSOCL=highestSOCL+1
        SOCLup = 'Level up! You are now on level ' + str(highestSOCL) + '. Good job!'
        print(typewriter(''.join(SOCLup)))
        with open('UserAccounts/'+nickname+'/SquareOrCubeLevel.md','w') as SOCLfile:
            SOCLfile.write(str(highestSOCL))
    SwitchMode()
def typewriter(t):
  for x in t:
    print(x, end='')
    sys.stdout.flush()
    sleep(random.uniform(0,speed))
nickname =input('Hello! Enter a nickname to save progress.\nIf you have used this tool before, enter the nickname you used last.\n')
if not os.path.exists('UserAccounts/'+nickname):
    os.mkdir('UserAccounts/'+nickname)
SOCLfile = open('UserAccounts/'+nickname+'/SquareOrCubeLevel.md','a+')
SOCLfile.close()
PLfile=open('UserAccounts/'+nickname+'/PrimeLevel.md','a+')
PLfile.close()
createTSfile=open('UserAccounts/'+nickname+'/TypeSpeed.md','a+')
createTSfile.close()
with open('UserAccounts/'+nickname+'/TypeSpeed.md','r+')as typespeed:
  TSread=typespeed.read() 
if TSread=='':
  write=input('Do you want to turn on typewriter effects?')
  if write.lower()=='yes':
    speed=float(input('Type a number to change speed of typewriter effect.\nNote that a lower amount means a higher speed, because it is measured  in average seconds delay between each letter.\nPress code, or go to\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff#readme\nfor more information.\n'))
    typewriter('This is how fast the effect will be. Are you happy with your changes?\n')
    happy=input()
    while happy.lower()=='no':
      typewriter('Type a number to change speed.\n')
      speed=input()
      typewriter('This is how fast the effect will be. Are you happy with your changes?\n')
      happy=input()
  else:
    speed=0
  with open('UserAccounts/'+nickname+'/TypeSpeed.md','w')as typespeed:
    typespeed.write(str(speed*2))
else:
  speed=float(TSread)
global SwitchMode
def SwitchMode():
  global start
  if start =='':
    typewriter('Hello, '+nickname+'. This is a tool to find more about numbers. What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a quiz about squares and cubes.\nType 7 to change typewriter effect speed!\nPlease click code, or visit\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff#readme\nfor more information.\nPlease report any bugs or feedback in the comments below, or on\nhttps://github.com/noneofyourbusiness1415252/Maths-stuff/issues\n')
    start=input()
  else:
    typewriter('Do you want to switch modes?\n')
    switch=input()
    if switch.upper()=='YES':
      typewriter('What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a quiz about squares and cubes.\n')
      start=input()
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
  elif start=='7':
    typewriter('Do you want to turn on typewriter effects?')
    write=input()
    if write.lower()=='yes':
      typewriter('Type a number to change speed of typewriter effect.\nNote that a lower amount means a higher speed, because it is measured  in average seconds delay between each letter.\n')
      speed=float(input())
      typewriter('This is how fast the effect will be. Are you happy with your changes?\n')
      happy=input()
      while happy.lower()!='yes':
        speed=float(input('Type a number to change speed.\n'))
        typewriter('This is how fast the effect will be.Are you happy with your changes?\n')
        happy=input()
      with open('UserAccounts/'+nickname+'/TypeSpeed.md','w')as TSFile:
        TSFile.write(str(speed))
      SwitchMode()
  else:
    start=input('Invalid option. Please type a number from 1 to 7 to choose a mode.\n')
SwitchMode()





