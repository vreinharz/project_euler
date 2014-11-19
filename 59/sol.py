import sys
from itertools import cycle, product
from string import lowercase, ascii_letters, digits


def decode(l, key):
    possible = ascii_letters + " ,.!?;'\n()" + digits
    c = cycle(key)
    message = ''.join(chr(ord(c.next())^x) for x in l)
    if all(x in possible for x in message):
        print key
        print message
        print sum(ord(x) for x in message)
        sys.exit(0)
        
def main():
    data = [int(x.strip()) for x in open('p059_cipher.txt').readline().split(',')]
    for x,y,z in product(lowercase, repeat=3):
        decode(data, x+y+z)
if __name__ == '__main__':
    main()
