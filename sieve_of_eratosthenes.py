# Hiya Jain
# Lab 08: Sieve of Eratosthenes
# CISC 1800 - Introduction to Computer Programming

def sieve_of_eratosthenes(limit):
  primes = [True] * (limit + 1)
  primes[0] = False
  primes[1] = False
  p = 2
  while p*p <= limit:
    if primes[p]:
      for i in range(p*p, limit + 1, p):
        primes[i] = False
    p += 1
    
  prime_numbers = [q for q, is_prime in enumerate(primes) if is_prime]
  return prime_numbers

#testing case
prime_numbers = sieve_of_eratosthenes(100)
print(prime_numbers)
