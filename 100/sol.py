def check_correct(tot):
    for blue in range(int(tot/2),tot):
        if 2*blue*(blue-1) == tot*(tot-1):
            return blue
    return None

if __name__ == '__main__':
    tot = 10**3
    while True:
        tot +=1
        blue =  check_correct(tot)
        if blue:
            print blue
            break



