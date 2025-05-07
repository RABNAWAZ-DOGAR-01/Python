num = input("Enter a number:")


if num == num[ ::-1 ]:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome")