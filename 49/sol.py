from trivial_generator import primes
from itertools import combinations

def all_permutations(x,y,z):
    if (sorted(str(x)) == sorted(str(y)) and
        sorted(str(x)) == sorted(str(z))):
        return True
    return False

def main():
    l = []
    for p in primes(): 
        if 1000 < p < 10000:
            l.append(p)
        elif p >= 10000:
            break
    print l
    for i, x in enumerate(l):
        print x
        for j,y in enumerate(l[i+1:]):
            for z in l[i+j+1:]:
                d1 = y-x
                d2 = z-y
                if x != 1487 and d1 == d2 and all_permutations(x,y,z):
                    print x,y,z
                    return
                if d2 > d1:
                    break

if __name__ == '__main__':
    main()
