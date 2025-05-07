numbers = list(map(int, input("Enter a list: ").split(",")))

# Remove duplicates while maintaining order
unique_numbers = list(dict.fromkeys(numbers))

# Convert to tuple & set
unique_numbers_set = set(unique_numbers)
unique_numbers_tuple = tuple(unique_numbers)

# Print results
print("Ordered List Without Duplicates:", unique_numbers)
print("Unique Numbers Set:", unique_numbers_set)
print("Final Tuple:", unique_numbers_tuple)
