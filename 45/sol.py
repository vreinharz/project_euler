from math import floor , ceil

def tri(i):
    return i*(i+1)/2

def is_tri(t):
    n =  int(ceil(((8*t-1)**0.5-1)*0.5))
    return t == tri(n)

def pen(i):
    return i*(3*i-1)/2

def is_pen(p):
    n = floor((1.0+(1+24*p)**0.5)/6)
    return p == pen(n)

def hex(i):
    return i*(2*i-1)

if __name__ == '__main__':
    for i in range(143, 100000):
        h = hex(i)
        if is_pen(h) and is_tri(h):
            print h
