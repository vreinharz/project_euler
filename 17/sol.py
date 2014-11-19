def nb_to_word(n):
    d = {0: '',
         1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five' ,
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine',
         10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen',
         20: 'twenty',
         30: 'thirty',
         40: 'forty',
         50: 'fifty',
         60: 'sixty',
         70: 'seventy',
         80: 'eighty',
         90: 'ninety',
         100: 'hundred',
         1000: 'thousand'}
    if n == 100:
        return 'onehundred'
    if n in d:
        return d[n]

    n_str = str(n)
    l = len(n_str)
    if l == 2:
        return d[int(n_str[0]+'0')] + d[int(n_str[1])]
    elif l == 3:
        w = d[int(n_str[0])] + d[100]
        if n_str[1:] == '00':
            return w
        else:
            w = w + 'and'
        if int(n_str[1:]) in d:
            return w + d[int(n_str[1:])]
        else:
            return w+d[int(n_str[1]+'0')] + d[int(n_str[2])]


if __name__ == '__main__':
    for n in range(1,1001):
        print nb_to_word(n)
    print sum(len(nb_to_word(n)) for n in range(1,1001))
