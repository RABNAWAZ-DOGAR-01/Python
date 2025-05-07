print("Problem 1: Write a program to find the largest of three numbers.")
a = int(input("Enter your number :"))
b = int(input("Enter your number :"))
c = int(input("Enter your number :"))

if a > b and a > c:
    print(f"largest number is A {a}")
elif b > a and b > c:
    print(f"largest number is B {b}")
else:
    print(f"largest number is C {c}")