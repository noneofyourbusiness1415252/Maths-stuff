def PrimeorComposite(n):
  if n == 2 or n == 3:
    return('is a prime number.')
  if n < 2 or n%2 == 0:
    return('is a composite number.')
  if n < 9:
    return('is a prime number.')
  if n%3 == 0:
    return('is a composite number.')
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0:
      return('is a composite number.')
    if n % (f+2) == 0:
      return('is a composite number.')
    f += 6
  return('is a prime number.')
def SquareorCube(n):
  if abs(n**(1/6)) == int(abs(n**(1/6))):
    return('is a power of 6, so it is both a square number and a cube number.')
  elif abs(n**0.5) == int(abs(n**0.5)):
    return('is a square number.')
  elif abs(n**(1/3)) ==int(abs(n**(1/3))):
    return('is a cube number.')
  else:
    return('is not a square or cube number.')
