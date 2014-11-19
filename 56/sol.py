def sum_digit(n):
    return sum(int(x) for x in str(n))

def main():
    m = 0
    for i in range(100):
        for j in range(100):
            s = sum_digit(i**j)
            m = s if s > m else m
    print m

if __name__ == '__main__':
    main()
