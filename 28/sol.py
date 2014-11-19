if __name__ == '__main__':
    tot = 1
    last = 1
    k = 0
    while k < 1000:
        k += 2
        for i in range(4):
            last += k
            tot += last
    print tot
