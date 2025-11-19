start_Index = int(input("Enter start index: "))
end_Index = int(input("Enter end index: "))
for num in range(start_Index, end_Index + 1):
    if num % 2 == 0:
        print(f"The first even number in the range is: {num}")
        break