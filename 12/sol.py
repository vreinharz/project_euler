def nb_div(n):
    i = 1
    div = {i,n}
    while i < n**(0.5):
        if n % i == 0:
            div.add(i)
            div.add(n/i)
        i += 1


    return sorted(list(div))

if __name__ == '__main__':

    n = 1
    max = 1
    l = nb_div(1)
    print l
    while True:
        n += 1
        t_l = nb_div(sum(range(n+1)))
        if len(t_l) > len(l):
            max = n
            l = t_l
            print max, len(l)
