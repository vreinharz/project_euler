def m_pandig(a,b,n):
    s = str(a) + str(b) + str(a*b)
    if len(s) == n and all(str(i) in s for i in range(1,n+1)):
        return True
    return False

def nb_pandig(n):
    i = 0
    tot = set()
    while True:
        i += 1
        j = i+1
        if len(str(i)+str(j)+str(i*j)) > n:
            break
        while True:
            if len(str(i)+str(j)+str(i*j)) > n:
                break
            elif m_pandig(i,j,n):
                print      i,j,i*j
                tot.add(i*j)
            j += 1
    return sum(tot)



if __name__ == '__main__':
    print nb_pandig(9)
