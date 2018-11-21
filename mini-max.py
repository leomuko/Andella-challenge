def mini_max():
    try:
        a, b, c, d, e = raw_input('Enter 5 spaced integers: ').split()
        a, b, c, d, e = [int(a),int(b),int(c),int(d),int(e)]    
        numbers = [a,b,c,d,e]
        numbers.sort()
        max = sum(numbers[1:])
        min = sum(numbers[:(len(numbers)- 1)])
        final = [str(min), str(max)]
        return ' '.join(final)
    except ValueError:
        print('Please enter 5 numbers and ensure they are spaced')
        return     


print(mini_max())

