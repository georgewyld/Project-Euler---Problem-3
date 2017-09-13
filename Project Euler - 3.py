#largest prime factor of 600851475143
import math, time
def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else: return False
    return True
def get_prime_factors(num):
    factors1=[]
    factors2=[]
    primes=[]
    for i in range (1,math.ceil(num**0.5+1)):
        if (num%i==0):
            factors1.append(i)
    for i in factors1:
        factors2.append(num/i)
    factors=list(map(int,factors1+factors2))
    factors.sort()
    for y in factors:
        if is_prime_number(y):
            primes.append(y)       
    return max(primes)
num=int(input('Which number do you wish to find the largest prime factor of? '))
start=time.time()
print(get_prime_factors(num))
elapsed=(time.time()-start)
print(elapsed)


