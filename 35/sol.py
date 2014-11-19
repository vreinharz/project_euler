from primes import primes

def circulate(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:]+s[:i])


if __name__ == '__main__':
    tot = {x:1 for x in primes(80000) if x < 10**6} #1million in first 80K
    res = 0
    for x in tot:
        if all(y in tot for y in circulate(x)):
            print x
            res += 1

    print '\t', res
