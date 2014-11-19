from pprint import pprint
from math import fsum, ceil
import sys

def is_prime(x):
    if x == 1:
        return False
    if x % 2 == 0:
        return False
    for j in range(3, int(ceil(x**0.5))+1):
        if x % j == 0:
            return False
    return True

def ratio_dag(d, before):
    nb = fsum(1 for x in d if is_prime(x)) + before[0]
    diag = 4. + before[1]
    return nb, diag

def spiral(n):
    d = {(0,0):1}
    v = 1
    before = (0., 1.)
    for i in range(1,n):
        start = min([x for x in d.keys() if x[0] == max(d.keys())[0]], key=lambda x:x[1])
        x, y = start
        for j in range(-i+1, i+1):
            v += 1
            d[x+1,j] = v
        y = j
        for j in range(y-1,-y-1,-1):
            v += 1
            d[j,y] = v
        x = j
        for j in range(abs(x)-1, x-1, -1):
            v += 1
            d[x,j] = v
        y = j
        for j in range(y+1, abs(y)+1):
            v += 1
            d[j,y] = v
        before = ratio_dag(d, before)
        b = before[0] / before[1]
        print b, max(d.keys())[0]*2 +1
        if b < 0.1:
            sys.exit(0)

def corner_spiral():
    v = 1
    before = (0., 1.)
    i = 0
    while True:
        i += 1
        corners = []
        length = 2*i
        for j in range(1,5):
            v += length
            corners.append(v)
        before = ratio_dag(corners, before)
        if before[0]/before[1] < 0.1:
            print before, length+1
            sys.exit(0)

def main():
    corner_spiral()

if __name__ == '__main__':
    main()
