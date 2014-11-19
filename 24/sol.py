import itertools
if __name__ == '__main__':
    print ''.join(sorted(itertools.permutations([str(x) for x in range(10)]))[10**6-1])
    
