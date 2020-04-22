def discounts(price, rate):
    final_price = price * rate
    old_price = 88 #Try to modify global variable
    print('old_price after modification: ', old_price)
    return final_price

old_price = float(input('Original Price is: '))
rate = float(input('Discount is: '))
new_price = discounts(old_price, rate)
print('old_price after modification: ', old_price)
print('Price after discount: ', new_price)
