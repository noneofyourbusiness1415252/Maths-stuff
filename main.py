start = input('Hello. This is a tool to find more about numbers. What do you want to do? Type in a number to go to one of these modes: \nType 1 to find out if a number is prime or composite. \nType 2 to find out how many Prime numbers are between 2 numbers\nType 3 to find out if a number is squared or cubed.\nType 4 to find out how many squares and cubes there are between 2 numbers.\n')
from PrimeorComposite import *
from SquareorCube import *
from SwitchMode import SwitchMode
while start == '1': 
  number = input('Enter a number.') 
  print(number, PrimeorComposite(int(number)))
  SwitchMode()
while start == '2':
    num1 = int(input('Enter the first number\n'))
    num2 = int(input('Enter the second number\n'))
    amount = 0
    primes = ('these are the prime numbers between',num1,'and', num2,':')
    for l in range (num1,num2+1):
      if PrimeorComposite(l) =='is a prime number.':
        amount = amount + 1
        primes = primes,str(l)
    if amount == 1:
      print('there is 1 prime number between',num1, 'and', num2)
    else:
      print('there are', amount, 'prime numbers between', num1, 'and', num2)
    print(primes)
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
  cubenums = 'The cube numbers between ', num1,'and',num2,'are:'
  squarenums = 'The square numbers between', num1, 'and',num2,'are:'
  for l in range (num1,num2+1):
    if SquareorCube(l)=='is both a square number and a cube number.':
      squares = squares + 1
      cubes = cubes + 1 
      squarenums = squarenums,str(l)
      cubenums = cubenums,str(l) 
    elif SquareorCube(l)=='is a cube number.':
      cubes = cubes + 1
      cubenums = cubenums,str(l)
    elif SquareorCube(l)=='is a square number.':
      squares = squares + 1
      squarenums = squarenums,str(l)  
  print('There are',cubes,'cube numbers, and',squares,'square numbers between',num1, 'and',num2,'.')
  print(cubenums,'\n',squarenums)
  SwitchMode()