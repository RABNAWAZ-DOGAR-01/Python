def remove_duplicates(nums):
    unique_list = []
    seen = set()
    for num in nums:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)
    return unique_list

# Example usage:
nums = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(remove_duplicates(nums))
