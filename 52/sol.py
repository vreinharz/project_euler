def check_val(nb):
    list_nb = sorted(list(str(nb)))
    for x in range(2,7):
        list_test = sorted(list(str(x*nb)))
        if list_test != list_nb:
            return False
    else:
        return True

if __name__ == '__main__':
    nb = 1
    while True:
        nb +=1
        if check_val(nb):
            print nb
            break

