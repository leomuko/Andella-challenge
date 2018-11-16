import sys
q = '1 2 3 4 5'
def mini_max():
    a, b, c, d, e = raw_input('Enter 5 spaced integers: ').split()
    a, b, c, d, e = [int(a),int(b),int(c),int(d),int(e)]
    numbers = [a,b,c,d,e]
    numbers.sort()
    max = sum(numbers[1:])
    min = sum(numbers[:(len(numbers)- 1)])
    final = [str(min), str(max)]
    return ' '.join(final)


print(mini_max())

