def primes():
    yield 2
    primes = [2]
    i = 2
    while True:
        i += 1
        if all(i%p != 0 for p in primes):
            primes.append(i)
            yield i
