def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('The greatest common divisor of %d is %d' % (num, count))
            break
        count -= 1
    else:
        print('%d is prime number !' % num)

num = int(input('Please input an integer: '))
showMaxFactor(num)
