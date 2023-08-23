val1 = int(input("Enter the first value: "))
val2 = int(input("Enter the second value: "))
val3 = int(input("Enter the third value: "))
val4 = int(input("Enter the fourth value: "))
val5 = int(input("Enter the fifth value, anything but 0: "))
value = val1 + (val2 - val3 * val4) / val5
print("{} + ({} - {} * {})/{} is {}".format(val1, val2, val3, val4, val5, value))
