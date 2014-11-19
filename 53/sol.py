import sys
import gmpy2

tot = 0
for n in range(23, 101):
    for i in range(n):
        if gmpy2.comb(n,i) > 10**6:
            tot += 1
print tot
