def PrimeorComposite(n):
  for i in range(2,int(n**0.5+1)):
    if abs(n%i) == 0 or n==0 or n==1:
      return('is a composite number.')
    else:
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
def SwitchMode():
  switch = input('Do you want to switch modes?\n')
  if switch.upper()=='YES':
    from main import start