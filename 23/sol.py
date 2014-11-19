import itertools
from math import floor 
import sys


def is_abundant(n):
    tot = 0
    i = 1
    while i < n :
        if n % i == 0:
            tot += i 
        i += 1
    return tot > n

if __name__ == '__main__':
    abundants = (x for x in xrange(1,28124) if is_abundant(x))
    sum_set = {x+y for x,y in itertools.product(abundants,repeat=2) if x+y < 28125}
    print sum(x for x in xrange(28124) if not x in sum_set)

