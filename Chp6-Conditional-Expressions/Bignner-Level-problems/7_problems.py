import math

num = int(input("Enter a number:"))

sqrt = math.sqrt(num)

if sqrt == int(sqrt):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")