def facterials(n):
    result = 1
    for i in range( 1 , n + 1):
        result *= i
    return result

print(facterials(5))





# Method 2: Using Recursion (Function Calls itself)

def factorials(n):
    if n == 0 or n == 1:
        return 1
    return n * facterials(n - 1)

# Example 
print(facterials(5))