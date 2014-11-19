import sys 
from math import floor
import itertools

def pen(i):
    return i*(3*i-1)/2

def gen_pen(max_val):
    i = 0
    while i < max_val:
        i += 1
        yield pen(i)

def is_pen(p):
    n = floor((1.0+(1+24*p)**0.5)/6)
    return p == pen(n)

if __name__ == '__main__':
    max_val = 5000
    for i in range(1, max_val):
        for j in range(i+1, max_val):
            p1, p2 = pen(i), pen(j)
            if is_pen(p2-p1) and is_pen(p1+p2):
                print p2-p1
                print p1, p2, i, j
                sys.exit(0)
         
