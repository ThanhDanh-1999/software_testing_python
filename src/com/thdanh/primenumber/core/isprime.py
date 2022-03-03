def isprime(n):
  if n < 0:
    # negative number is not prime
    # exception: ValueError (n < 0) is raised by isprime() function in isprime.py file 
    raise Exception("prime() not defined for negative values...")
  else:
    if (n==1) or (n==0):
      return False # return False if n is 1 or 0
    for i in range(2,n):
      if(n % i==0):
        return False # return False if n is divisible by any number other than 1 and itself 
    else:
      return True # return True if n is prime 
