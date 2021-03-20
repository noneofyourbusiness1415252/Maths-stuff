def PrimeorComposite(n):
  if n == 1 or n == 0:
    return('is a composite number.')
  else:  
    for i in range(2, int(n**0.5)+1):
      if n % i == 0:
            return ('is a composite number. ')
  return ('is a prime number.')