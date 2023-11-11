"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import log2
def primes(number_of_primes):
    reng=2*number_of_primes/log2(number_of_primes)
    list = []
    primes = []
    for i in (2,reng):
        list.append(i)
    primes.append(2)
    for i in (2,reng):
        if i in list:
            primes.append(i)
            for x in list.copy():
                if x%i==0:
                    list.remove(x)
    return primes[0:number_of_primes]

def __init__():
    print(primes(100))