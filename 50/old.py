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
    start = time.time()
    primes_gen = primes()
    nb = primes_gen.next()
    primes_list = [nb]
    nb = primes_gen.next()
    max = 0
    while nb < 10**6:
        l = slice_sub_equal(nb, primes_list)
        if l and l > max:
            print nb
            best = nb
            max = l
        primes_list.append(nb)
        nb = primes_gen.next()
    print 'all that in: ', time.time() - start, 'seconds'
    print best, max
