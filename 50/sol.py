from trivial_generator import primes
import multiprocessing 
import sys
m = 10**6
p = primes()
l = []
while True:
    n = p.next()
    if n < m:
        l.append(n)
    else:
        break



def max_consecutive_sum(p):
    for i in range(len(l)):
        tot = 0
        nb = 0
        while tot < p and l[i] < p:
            tot += l[i+nb]
            nb += 1
        if tot == p:
            return nb, p
    return 0, p

def main():
    sol = 0
    m = 0
    pool = multiprocessing.Pool(processes=4)
    for nb, p in pool.imap_unordered(max_consecutive_sum, l):
        if nb > m:
            m, sol = nb, p
    return sol

if __name__ == '__main__':
    print main()
