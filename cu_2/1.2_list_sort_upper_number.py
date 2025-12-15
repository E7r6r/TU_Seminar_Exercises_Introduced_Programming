list_test  = input ("Enter numbers separated by spaces: ").split()
list_numbers = int []

while n > 0:
    for i in range(n):
        if list_numbers[i] > list_numbers[i+1]:
            temp = list_numbers[i]
            list_numbers[i] = list_numbers[i+1]
            list_numbers[i+1] = temp
    n = n - 1  
print("Sorted list in ascending order is:", list_numbers)   
   