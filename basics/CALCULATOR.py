p = float(input("Enter the percentage of your marks: "))
if p >= 90.:
    print("Got an Outstanding Grade")
elif 75. <= p < 90.:
    print("Got an A Grade")
elif 60. <= p < 75.:
    print("Got a B Grade")
elif 45. <= p < 60.:
    print("Got a C Grade")
else:
    print("Got an F Grade")