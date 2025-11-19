num = int(input("Enter a number: "))
for n in range(num,1, -1):
    if (num % n == 0):
        print(f"Divisor of the number is: {n}")