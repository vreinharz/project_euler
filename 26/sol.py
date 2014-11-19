def length_cycle(n):
    list_digits = []
    nb = 1
    while True:
        while nb < n:
            nb = nb * 10
        if nb in list_digits:
            return len(list_digits)-list_digits.index(nb)
        list_digits.append(nb)
        nb = nb % n
        if nb == 0:
            return 0

if __name__ == '__main__':
    print max(((i,length_cycle(i)) for i in range(1,1001)),key=lambda x:x[1])

