a = input("This programm calculates the greater common divisor of two given integers.\nAt least one number must not be zero. You have to enter two numbers.\nEnter the first one> ")
b = input("Enter the second one> ")

while (a == b == 0) or not a.isdigit() or not b.isdigit():
    a = input("Entered numbers are incorrect, please enter the correct numbers.\nEnter the first one> ")
    b = input("Enter the second one> ")

a = abs(int(a))
b = abs(int(b))
a, b = max(a,b), min(a,b)
if b == 0:
    print(f"The greater common divisor of entered numbers is {a}.")
else:
    while a % b != 0:
        a, b = max(a % b, b), min(a % b, b)
    print(f"The greater common divisor of entered numbers is {b}.")