def sum_power(n,p):
    tot = 0
    for i in str(n):
        tot += (int(i)**p)
        if tot > n:
            return False
    if tot == n:
        return True
    else:
        return False

if __name__ == '__main__':
    print sum(i for i in range(2,10**6) if sum_power(i,5))
