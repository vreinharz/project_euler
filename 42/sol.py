from math import floor, ceil

def word_triang(w):
    s = sum( 1.0+ord(x)-ord('A') for x in w)
    n = (-1+(1+8*s)**0.5)/2
    if not floor(n) < n < ceil(n):
        return True
    return False
        

if __name__ == '__main__':
    list = eval(open('words.txt', 'r').readline())
    t = 0
    for x in list:
        if word_triang(x):
            t+=1
    print t
