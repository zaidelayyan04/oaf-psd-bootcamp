def isprime(n):
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  for i in range(5, int(n**.5) + 1, 6):
    if n % i == 0 or n % (i+2) == 0:
      return False
  return True
