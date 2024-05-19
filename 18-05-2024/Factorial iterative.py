factorial = 1
number = int(input("Enter the Number"))
if number < 0:
    print("Factorial doest not exist for negative Number")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
        print("factorial  of", number, "is", factorial)
