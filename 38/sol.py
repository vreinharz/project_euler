def mult_pan_digital(n):
    i = 0
    pan = ''
    while len(pan) < 9:
        i += 1
        pan += str(i*n)
    if len(pan) == 9 and all(x in pan for x in ('1','2','3','4',
                                               '5','6','7','8','9')):
        return int(pan)
    else:
        return None

if __name__ == '__main__':
    max_pan = 0
    i = 0
    while i < (10**10):
        i += 1
        pan = mult_pan_digital(i)
        if pan and pan > max_pan:
            max_pan = pan
            print max_pan
    print '\t', max_pan
