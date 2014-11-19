import math

if __name__ == '__main__':
    i = 3
    while True:
        if sum(math.factorial(int(x)) for x in str(i)) == i:
            print i
        i += 1
