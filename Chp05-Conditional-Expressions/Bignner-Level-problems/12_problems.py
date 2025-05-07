def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))  # Convert string to list of integers
    return f"{max(num_list)} {min(num_list)}"  # Find max and min, return formatted string

# 🔹 User se input lena
user_input = input("Enter space-separated numbers: ")  

# 🔹 Function ko call karna aur output print karna
print(high_and_low(user_input))
