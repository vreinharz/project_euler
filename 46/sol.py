from trivial_generator import primes
from math import floor
import sys

i = 3
while True:
    i += 2
    found_sol = False
    for j in primes():
        if j == i:
            break
        elif j > i:
            print i
            sys.exit(0)
        for k in range(1,int(floor(i**0.5))):
            if 2*(k**2)+j == i:
                found_sol = True
                break
        if found_sol:
            break
