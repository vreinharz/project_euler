import sys

def find_prime_factors(n):
    i = 2
    factors = set()
    while n > 1:
        while n % i == 0:
            factors.add(i)
            n /= i
        i += 1
    return factors

def consecutive_diff_factors(n, target):
    out = target
    for i in range(n+target-1, n-1, -1):
        if len(find_prime_factors(i)) == target:
            out -= 1
    return out


if __name__ == '__main__':
    i = 2
    while True:
        out = consecutive_diff_factors(i,4)
        if out == 0:
            print i
            break
        i += out
