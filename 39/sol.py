def nb_triangle_perim(n):
    sols = set()
    for x in range(1,n):
        for y in range(x,n-x):
            z = n - x - y
            if z**2 == x**2 + y**2:
                sols.add(tuple(sorted([x,y,z])))
    return len(sols)


if __name__ == '__main__':
    max_nb = 0
    max_n = 0
    for i in range(1001):
        n = nb_triangle_perim(i)
        if n > max_nb:
            max_nb = n
            max_n = i
            print max_n, max_nb
    print max_n, max_nb

