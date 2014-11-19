import time

def primes():
    nb = 2
    yield nb
    primes = [nb]
    while True:
        nb += 1
        if all(nb % x != 0 for x in primes):
            yield nb
            primes.append(nb)

def slice_sub_equal(nb, to_slice):
    for i,j in ((x,y) for x in range(len(to_slice))
                      for y in range(len(to_slice)+1)
                        if y > x):
        if sum(to_slice[i:j]) == nb:
            return j - i
    return None


if __name__ == '__main__':
    g = primes()
    a = g.next()
    while a < 10**6:
        a = g.next()
        print a
