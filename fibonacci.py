# fibonacci 1

def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('Wrong Input! ')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    
    return n3

number = int(input('Please input an integer: '))
result = fab(number)
if result != -1:
    print('There are totally %d rabbit born! ' % result)


# fibonacci 2

def fab(n):
    if n < 1:
        print('Wrong Input! ')
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

number = int(input('Please input an integer: '))
result = fab(number)
if result != -1:
    print('There are totally %d rabbit born! ' % result)
