def combinatorial(n,r):
    res = 1
    for x in range(n,r,-1):
        res *= x
    div = 1
    for x in range(1,r+1):
        div *= x
    return res / div

if __name__ == '__main__':
    print combinatorial(40,20)
