#Go to README.md for guidance on how to use this program. 
from PrimeorComposite import *
from SquareorCube import *
from SwitchMode import *
import random
squareorcubelevel = 1
primelevel = 1
start = input('Hello. This is a tool to find more about numbers. What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\nType 5 for a quiz about primes and composites.\nType 6 for a quiz about squares and cubes.\nPlease go to code, thenn go to README.md for guidance and information.\n') 
while start == '1': 
  number = input('Enter a number.') 
  print(number, PrimeorComposite(int(number)))
  SwitchMode()
while start == '2':
    num1 = int(input('Enter the first number\n'))
    num2 = int(input('Enter the second number\n'))
    amount = 0
    primes = ('these are the prime numbers between' +str(num1) +' and '+ str(num2) +': ')
    for l in range (num1,num2+1):
      if PrimeorComposite(l) =='is a prime number.':
        amount = amount + 1
        primes = primes+str(l)+', ' 
    if amount == 1:
      print('there is 1 prime number between',num1, 'and', num2)
    else:
      print('there are', amount, 'prime numbers between', num1, 'and', num2)
    Total= ''. join(primes)
    print(Total)
    SwitchMode()
while start == '3':
   number =  int(input('Enter a number to find whether it is squared or cubed!\n'))
   print(number,SquareorCube(number))
   SwitchMode()
while start =='4':
  num1 = int(input('Enter the first number\n'))
  num2 = int(input('Enter the second number.\n'))
  cubes = 0
  squares = 0
  cubenums = 'The cube numbers between '+ str(num1) +' and '+str(num2) +' are: '
  squarenums = 'The square numbers between '+ str(num1) + ' and '+str(num2)+' are: '
  for l in range (num1,num2+1):
    if SquareorCube(l)=='is a power of 6, so it is both a square number and a cube number.':
      squares = squares + 1
      cubes = cubes + 1 
      squarenums = squarenums+str(l)+', ' 
      cubenums = cubenums+str(l)+', '
  for l in range (num1,num2+1):
    if SquareorCube(l)=='is a cube number.':
      cubes = cubes + 1
      cubenums = cubenums+ str(l)+', '
  for l in range (num1,num2+1):
    if SquareorCube(l)=='is a square number.':
      squares = squares + 1
      squarenums = squarenums+str(l)+', '  
  total = ('There are ',str(cubes),' cube numbers, and ',str(squares),' square numbers between ',str(num1), ' and ',str(num2),'.')
  print(''.join(total))
  totallist = cubenums+'\n' +squarenums
  print(''.join(totallist))
  SwitchMode()
while start == '5':
  score = 0
  for a in range(10):
    if primelevel==1:
      rand =random.randint(1,10)
    else:
      rand = random.randint(primelevel**2*10-(primelevel-1)**2*10,primelevel**2*10)
    text = 'Is ',str(rand),' a prime number?\n'
    answer = input(''.join(text))
    if PrimeorComposite(rand)=='is a prime number.':
      if  answer.upper()=='YES':
        print('Well done!')
        score = score +1 
      else:
        print('Oops. Incorrect answer!')
    else:
      if answer.upper()=='NO':
        print('Well done!')
        score = score + 1
      else:
        print('Oops. Incorrect answer!')
  if score>9:
    primelevel = level + 1
    primelevelup = 'Level up! You are now on level ',str(primelevel),'! Good work! You will now get harder questions!'
    print(''.join(primelevelup))
    SwitchMode() 
while start == '6':
  score = 0
  powers = 0
  for a in range(9):
    if squareorcubelevel==1:
      randnum=random.randint(1,10)
    else:
      randnum=random.randint(squareorcubelevel**2*10-(squareorcubelevel-1)**2*10,squareorcubelevel**2*10)
    text = 'Is ', str(randnum)," a square number or cube number? Type 'both', 'square', 'cube' or 'no' accordingly. \n"
    answer = input(''.join(text))
    if SquareorCube(randnum)=='is a power of 6, so it is both a square number and a cube number.':
      if answer.upper() =='BOTH':
        print('Well done!!')
        score = score + 1
      else:
        print('Oops! Incorrect answer!')
    elif SquareorCube(randnum)=='is a square number.':
      if answer.upper() == 'SQUARE':
        print('Well done!')
        score = score + 1
      else:
        print('Oops! Incorrect answer.')
    elif SquareorCube(randnum)=='is a cube number.':
      if answer.upper() == 'CUBE':
        print('Well done!')
        score = score + 1
      else:
        print('Oops! Incorrect answer!')
    else:
      if answer.upper() =='NO':
        print('Well done!')
        score = score + 1
      else:
        print('Oops. Incorrect answer!')
  if score >9:
    squareorcubelevel = squareorcubelevel + 1
    squarecubelevelup ='Level up! You are now on level'+str(squareorcubelevel)+ '.Good job!'
    print(''.join(squarecubelevelup))
    SwitchMode()


