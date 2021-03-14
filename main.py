def isPrime(n):
  if n == 1:
    return('This is a composite number')
  else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return ('This is a composite number')
        
    return ('This is a prime number')
while True:
  number = int(input('Enter a number to see if it is prime or composite.'))
  print(isPrime(number))


