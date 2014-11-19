def gen_primes(n):
    p = [2]
    for i in range(3,n+1):
        if not any(i%x== 0 for x in p):
            p.append(i)

    return p

if __name__ == '__main__':
    TARGET = 20
    p = gen_primes(TARGET)
    min_decomp = [0]*len(p)
    for i in range(2,TARGET):
        decomp = [0]*len(p)
        k = 0
        while i != 1:
            while i % p[k] == 0:
                decomp[k] += 1
                i = i / p[k]
            k += 1
        for j in range(len(p)):
            min_decomp[j] = max(decomp[j],min_decomp[j])
    print min_decomp
    tot = 1
    for i in range(len(min_decomp)):
        tot = tot * (p[i]**min_decomp[i])
    print tot
