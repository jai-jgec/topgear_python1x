def prime(n):
  num = n
  if num > 2:
    for i in range(2,num):
      if (num % i) == 0:
        print(num,"is not a prime number")
        break
      else:
        print(num,"is a prime number")
  elif num == 2:
    print(num,"is a prime number")   
  else:
    print(num,"is not a prime number")

   
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

	
prime(2)
print get_primes(100)   