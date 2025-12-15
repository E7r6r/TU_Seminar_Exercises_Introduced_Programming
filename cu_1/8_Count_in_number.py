number = str(input("Enter a number: "))
counter =-0
number = number.lstrip("-+")
for digit in number:
    counter += 1

print(f"The number of digits in the number is: {counter}")