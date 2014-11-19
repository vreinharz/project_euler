if __name__ == '__main__':
    i = 0
    l = 0
    d = []
    d_to_find = tuple(10**n for n in range(7))
    print d_to_find
    while len(d) < len(d_to_find):
        i += 1
        s_i = str(i)
        new_l = l + len(s_i)
        if l < d_to_find[len(d)] <= new_l:
            d.append(s_i[d_to_find[len(d)]-l-1])
            print s_i
        l = new_l

    print d
    tot = 1
    for x in d:
        tot = tot*int(x)
    print tot
