num1 = int(input("Enter the Dividend: "))
num2 = int(input("Enter the Divisor: "))
rem = num1 % num2
if rem == 0:
    print("{} is divisible by {}".format(num1, num2))
else:
    print("{} is not divisible by {}".format(num1, num2))
