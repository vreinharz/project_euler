import itertools

def ways(n,coins=(200,100,50,20,10,5,2,1)):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    tot = []
    for j,c in enumerate(coins):
        i = 1
        if c == 1:
            tot += [[1]*n]
            break
        while (i)*c <= n:
            tot += [[c]*i + x for x in ways(n-i*c,coins[j+1:])]
            i += 1
    return tot

if __name__ == '__main__':
    print len(ways(200))

