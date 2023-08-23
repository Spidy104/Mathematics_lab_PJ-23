number = int(input("Enter the number whose multiplication table you want to print: "))
start = 1
while start <= 13:
    print("{} x {} is {}".format(number, start, (number * start)))
    start += 1
