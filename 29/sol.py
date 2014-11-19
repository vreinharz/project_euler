def to_the_power(power):
    for x in range(2,101):
        yield x**power

if __name__ == '__main__':
    a = set([])
    for x in range(2,101):
        a = a.union(set(to_the_power(x)))
    print len(a)

