def is_prime(nb):
    if nb < 1:
        return False
    for x in range(2, int(nb**(0.5))):
        if nb % x == 0:
            return False
            break
    else:
        return True

def consecutive_primes(a,b):
    tot = 0
    while True:
        next_val = tot**2 + tot * a + b
        if is_prime(next_val):
            tot +=1
        else:
            return tot

if __name__ == '__main__':
    max = 0
    for a,b in ( (x,y) for x in range(-1000,1000)
                       for y in range(-1000,1000)):
        tot = consecutive_primes(a,b)
        if tot > max:
            max = tot
            best = (a,b)
    print best, max
    print best[0] * best[1]


