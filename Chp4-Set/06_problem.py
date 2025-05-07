numbers = [1, 2, 3, 2, 4, 1, 3, 2, 4, 4, 5, 6, 6]

# Har unique element ka count find karna
freq = {num: numbers.count(num) for num in set(numbers)}

print("Frequency of elements:", freq)
