num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print("Power of Two")
else:
    print("Not a Power of Two")
