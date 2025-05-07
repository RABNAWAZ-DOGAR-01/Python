nums = list(map(int , input("Enter your numbers :").split()))

res = 0

for num in nums:
    res ^= num
    print(f"XOR of {res} and {num} is {res ^ num}")
    print(f"Result is {res}")