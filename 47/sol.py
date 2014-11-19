from trivial_generator import primes

def find_prime_factors(n):
    p = primes()
    i = p.next()
    factors = set()
    while n > 1:
        while n % i == 0:
            factors.add(i)
            n /= i
        i = p.next()
    return factors

def consecutive_diff_factors(n, target):
    if all(len(find_prime_factors(n+i)) == target for i in range(target)):
        return True
    else:
        return False

if __name__ == '__main__':
    i = 2
    while True:
        if consecutive_diff_factors(i, 4):
            print i
            break
        i += 1
