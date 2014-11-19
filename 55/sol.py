def rev_nb(n):
    n = str(n)
    return int(n[::-1])

def is_pal(n):
    n = str(n)
    return n == n[::-1]

def lychrel(n,t=50):
    n = n+rev_nb(n)
    if is_pal(n):
        return False
    elif t == 0:
        return True
    else:
        return lychrel(n, t-1)

def main():
    print sum(1 for i in range(10000) if lychrel(i))

if __name__ == '__main__':
    main()
