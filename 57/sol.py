import fractions


def main():
    tot = 0
    for i in range(1,1001):
        sub = 0
        for j in range(i):
            sub = fractions.Fraction(1, sub+2)
        approx = 1+ sub
        if len(str(approx.numerator)) > len(str(approx.denominator)):
            tot += 1
    print tot

if __name__ == '__main__':
    main()
