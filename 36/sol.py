def palyndrom(n):
    s = str(n)
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            return False
    return True

def base_10_to_2(n):
    best = 1
    while 2**best < n:
        best += 1
    b = []
    for i in range(best,-1,-1):
        if 2**i <= n:
            n -= 2**i
            b.append('1')
        else:
            b.append('0')
    return int(''.join(b))

if __name__ == '__main__':
    tot = 0
    for i in xrange(10**6):
        if palyndrom(i) and palyndrom(base_10_to_2(i)):
            print i, base_10_to_2(i)
            tot += i
    print '\t',tot
