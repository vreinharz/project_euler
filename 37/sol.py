from primes import primes

def gen_truncable(n):
    s = str(n)
    l = len(s)
    for i in range(l):
        left = s[:i]
        right = s[i:]
        if left:
            yield int(left)
        if right:
            yield int(right)

if __name__ == '__main__':
    p = {x:1 for x in primes(80000)} #all primes < 10**6
    sol = []
    print 'start'
    for n in p:
        if n < 10:
            continue
        for x in gen_truncable(n):
            if not x in p:
                break
        else:
            sol.append(n)
    print sum(sol), len(sol)
    for x in sol:
        print '\t', x
