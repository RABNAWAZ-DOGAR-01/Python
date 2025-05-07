n = int(input("Enter a number :"))


i = 1

while(i<11):
    print(f"{n} X {i} = {n * i}")
    i = i + 1


n = int(input("Enter the number :"))


i = 1

while(i<11):
    print(f"{n} x {i} = {n * i }")
    i = i +1 

# n = input("Enter number :")

# for num in  range(1 , 11):
#     print(f"{n} x {num} = {num * n}")

n = int(input("Enter number: "))  # Convert input to integer

for num in range(1, 11):
    print(f"{n} x {num} = {num * n}")  # Correct multiplication
