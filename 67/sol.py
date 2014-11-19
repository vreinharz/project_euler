if __name__ == '__main__':
    m = [[int(y) for y in x.strip().split(' ')] for x in open('triangle.txt').readlines()]
    tot = [[m[0][0]]]
    for row in m[1:]:
        tot.append([])
        for i, element in enumerate(row):
            best = 0
            if 0 <= i-1 < len(tot[-2]):
                new_val = element+tot[-2][i-1]
                if new_val > best:
                    best = new_val
            if 0 <= i < len(tot[-2]):
                new_val = element+tot[-2][i]
                if new_val > best:
                    best = new_val
            tot[-1].append(best)
    print max(tot[-1])
             
