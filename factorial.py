# factorial 1

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i

    return result

number = int(input('Please input an integer: '))
result = factorial(number)
print("The factorial of %d is %d" % (number, result))


# factorial 2

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('Please input an integer: '))
result = factorial(number)
print("The factorial of %d is %d" % (number, result))
