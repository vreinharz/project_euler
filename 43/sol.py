from itertools import permutations as permuts

def has_magic_property(s):
    if (int(s[1:4]) % 2 == 0 and
        int(s[2:5]) % 3 == 0 and 
        int(s[3:6]) % 5 == 0 and
        int(s[4:7]) % 7 == 0 and
        int(s[5:8]) % 11 == 0 and
        int(s[6:9]) % 13 == 0 and
        int(s[7:10]) % 17 == 0):
        return True
    return False

if __name__ == '__main__':
    tot = 0
    for x in permuts((str(y) for y in range(10))):
        x = ''.join(x)
        if has_magic_property(x):
            print x
            tot += int(x)
    print '\t', tot
