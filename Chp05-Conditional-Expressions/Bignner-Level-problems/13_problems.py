def categorize_members(members):
    result = []  # Empty list to store output

    for age, handicap in members:
        if age >= 55 and handicap > 7:
            result.append("Senior")  # If both conditions met, add "Senior"
        else:
            result.append("Open")  # Otherwise, add "Open"

    return result  # Return the final list

# 🔹 Example Test Case
input_data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = categorize_members(input_data)
print(output)

