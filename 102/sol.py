from itertools import combinations
def o_in_tr(a, b, c):
    l_nodes = [a,b,c]
    l_lines = [line(x,y) for x,y in combinations(l_nodes, 2)]
    magic = 10.**5
    N = max(intersect(line((0,0),(1, magic)), x)[1] for x in l_lines)
    S = min(intersect(line((0,0),(1, -magic)), x)[1] for x in l_lines)
    W = min(intersect(line((0,0),(-magic,0)), x)[0] for x in l_lines)
    E = max(intersect(line((0,0),(magic,0)), x)[0] for x in l_lines)
    print N, W, S, E
    if N > 0 and E > 0 and S < 0 and W < 0:
        return True
    return False

def line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    a = (y2-y1)/(x2-x1)
    b = -x1*a + y1
    assert (a*x1 + b - y1) < 0.1**10
    assert (a*x2 + b - y2) < 0.1**10
    return a, b

def intersect(line1, line2):
    a, b = line1
    c, d = line2
    #ax + b = cx + d
    #x(a-c) = d-b
    x = (d-b)/(a-c)
    y = a*x + b
    return x, y

if __name__ == '__main__':
    a = (-340, 495)
    b = (-153, -910)
    c = (835, -947)
    x = (-175, 41)
    y = (-421, -714)
    z = (574, -645)
    print o_in_tr(a,b,c)
    print o_in_tr(x,y,z)
