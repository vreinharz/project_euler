import sys
from itertools import permutations as permut
def is_prime(n):
    for x in xrange(2,int(n**0.5)+1):
        if n % x == 0: return False
    return True


if __name__ == '__main__':
    for y in xrange(10,1,-1): 
        for x in reversed(sorted(permut(xrange(1,y)))):
            int_x = int(''.join(str(z) for z in x))
            if is_prime(int_x):
                print int_x
                sys.exit(0)

