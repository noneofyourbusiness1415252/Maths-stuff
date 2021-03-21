def SquareorCube(n):
  if abs(n**(1/6)) == int(abs(n**(1/6))):
    return('is both a square number and a cube number.')
  elif abs(n**0.5) == int(abs(n**0.5)):
    return('is a square number.')
  elif int(abs(n**(1/3))) == abs(n**(1/3)):
    return('is a cube number.')
  else:
    return('is not a square or cube number.')

    