import os

with open('names.txt') as f:
    names = eval('(%s)' % f.readline())


names_val = []
for n in sorted(names):
    names_val.append(sum([ord(x) - 64 for x in n]))
tot = sum([ (i+1)*x for i,x in enumerate(names_val)])

print tot
