from fractions import Fraction

def is_weird(a,b):

    a1,a2 = [int(x) for x in str(a)]
    b1,b2 = [int(x) for x in str(b)]
    if b1 != 0 and a1 == b2 and Fraction(a,b) == Fraction(a2,b1):
        return True
    elif b2 != 0 and a2 == b1 and Fraction(a,b) == Fraction(a1,b2):
        return True
    return False

if __name__ == '__main__':
    for i in range(11,100):
        for j in range(i+1,100):
            if is_weird(i,j):
                print Fraction(i,j)
