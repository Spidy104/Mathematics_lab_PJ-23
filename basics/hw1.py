a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
while True:
    if b == 0:
        print('Enter another value, division by zero is not possible')
        b = int(input())
    else:
        break
add_value = a + b
sub_value = a - b
mult_value = a * b
div_value = a / b
power = a ** b
print("The addition of {} and {} is {}".format(a, b, add_value))
print("The subtraction of {} from {} is {}".format(b, a, sub_value))
print("The multiplication of {} and {} is {}".format(a, b, mult_value))
print("The division of {} by {} is {}".format(a, b, div_value))
print("{} raised to the power of {} is {}".format(a, b, power))
