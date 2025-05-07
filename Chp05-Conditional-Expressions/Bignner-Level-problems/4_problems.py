num = int(input("Enter a number: "))

if num % 5 == 0 or num % 11 == 0:
    print(f"{num} is divisible by 5 or 11")
else:
    print(f"{num} is not divisible by 5 or 11")
