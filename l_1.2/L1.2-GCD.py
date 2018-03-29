a = input("This programm calculates the greater common divisor of two given integers.\n"
          "At least one number must not be zero. You have to enter two numbers.\nEnter the first one> ")
b = input("Enter the second one> ")

# waiting for integer input: positive or negative
while not ((a.isdigit() or (a.startswith('-') and a[1:].isdigit()))
           and (b.isdigit() or (b.startswith('-') and b[1:].isdigit()))):
    a = input("Entered numbers are incorrect, please enter the correct numbers.\nEnter the first one> ")
    b = input("Enter the second one> ")

# reading our integers
a = abs(int(a))
b = abs(int(b))
# if both of them are 0, great common devisor is not defined
if a == b == 0:
    print('The great common divisor is not defined if both inputed integers equals zero.')
else:
    a, b = max(a,b), min(a,b)
    if b == 0:
        print(f"The greater common divisor of entered numbers is {a}.")
    else:
        while a % b != 0:
            a, b = max(a % b, b), min(a % b, b)
        print(f"The greater common divisor of entered numbers is {b}.")