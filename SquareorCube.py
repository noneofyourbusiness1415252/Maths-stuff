def SquareorCube(n):
  if n**0.5 == int(n**0.5):
    return('is a square number.')
  if int(n**(1/3)) == n**(1/3):
    return('is a cube number.')
  return('is not a square or cube number.')