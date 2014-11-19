from itertools import permutations
import sys
from math import floor, ceil

def palindromics():
    chars_digits = tuple(str(z) for z in xrange(10))
    for x in xrange(1,10):
        yield x
    for x in xrange(1,10):
        yield int(str(x) + str(x))
    for x in xrange(1,10):
        for y in chars_digits:
            yield int(str(x) + y + str(x))
    length = 4
    while True:
        for x in xrange(1, 10):
            for y in permutations(chars_digits, length / 2 -1):
                if length % 2 == 0:
                    pal = str(x) + ''.join(y) + ''.join(y[::-1]) + str(x)
                    yield int(pal)
                else:
                    for z in chars_digits:
                        pal = str(x) + ''.join(y) + z + ''.join(y[::-1]) + str(x)
                        yield int(pal)
        length += 1

def is_cons_ss(n):
    length = 1
    start = 1
    mins = 1
    maxs = 7
    minval = 1
    maxval = 670
    while True:
        if start ** 2 > n:
            return False
        length = (maxval + minval) / 2
        ss = sum_squares(start, start + length) 
        if ss == n:
            return True
        
        if ss > n:
            if  maxval == minval + 1:
                length = (maxval - minval) / 2 +1
                ss = sum_squares(start, start + length) 
                if ss == n:
                    return True
                minval = 1
                maxval = 670
                start += 1
            elif maxval == minval:
                minval = 1
                maxval = 670
                start += 1
            else:
                maxval = int(ceil(maxval + minval) / 2.)
        else :
            if  maxval == minval + 1:
                length = (maxval - minval) / 2 +1
                ss = sum_squares(start, start + length) 
                if ss == n:
                    return True
                minval = 1
                maxval = 670
                start += 1
            elif maxval == minval:
                minval = 1
                maxval = 670
                start += 1
            else:
                minval = (maxval + minval) / 2

def sum_squares(a,b):
    return sum(x**2 for x in xrange(a,b+1))

if __name__ == '__main__' :

    p = palindromics()
    t = []
    checkpoint = 1
    while True:
        n = p.next()
        if n > 10**checkpoint:
            print 'check', 10**checkpoint
            checkpoint += 1
        if n > 10**5:
            break
        test = is_cons_ss(n)
        if test:
            t.append(n)
print sum(t), len(t)
