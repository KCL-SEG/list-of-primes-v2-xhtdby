"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import log2,ceil
def primes(number_of_primes):
    if number_of_primes<0 or number_of_primes%1!=0:
        raise ValueError
    reng=ceil(2*number_of_primes/log2(number_of_primes))
    list = []
    primes = []
    for i in (2,reng):
        list.append(i)
    for i in (2,reng):
        if i in list:
            primes.append(i)
            for x in list.copy():
                if x%i==0:
                    list.remove(x)
    try:
        return primes[0:number_of_primes-1]
    except:
        return []