# User se input lena
user_input = input("Enter numbers separated by commas: ").strip()

# Split karke list me convert karna, phir set me convert karna (duplicates remove)
unique_numbers = set(map(int, user_input.split(",")))

# Sorted output
print("Unique sorted numbers:", sorted(unique_numbers))

