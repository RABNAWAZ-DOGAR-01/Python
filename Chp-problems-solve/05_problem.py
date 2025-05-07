numbers = [1 , 2, 10 , 20 , 40 , 99 , 88 , 24 , 23 , 22 , 21 , 20 , 10 , 2 , 1]


Even_numbers = []
Odd_numbers = []


for num in numbers:
    if num % 2 == 0:
        Even_numbers.append(num)
    else:
        Odd_numbers.append(num)


print("Even Numbers:", Even_numbers)
print("Odd Numbers:", Odd_numbers)
