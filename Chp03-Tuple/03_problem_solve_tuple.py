#  User se ek tuple ka input lo aur usko print karo.
# User se comma-separated input lena
# user_input = input("Enter numbers separated by commas: ")

# # Split karke tuple me convert karna
# my_tuple = tuple(map(int, user_input.split(",")))

# print("Your tuple:", my_tuple)



# Problem: Tuple Ke Even Numbers Print Karo
# Question: Ek tuple diya gaya hai, usme sirf even numbers print karo.
numbers = (10 , 20 , 30 ,504 , 73, 87 , 40 , 576 , 30 )

for num in numbers:
    if num %2 == 0:
        print("This is a even number", num)


# even_numbers = tuple(num for num in numbers if num % 2 == 0)

# print(even_numbers)

# Problem: Tuple Ka Largest & Smallest Number Find Karo
#  Question: Tuple ke maximum & minimum numbers find karo.
tuples = ( 10  , 20 , 30 , 40 , 50 ,60)
print(max(tuples))
print(min(tuples))



# Problem: Duplicate Hatao & Sorted Tuple Print Karo
# Question: Ek tuple diya gaya hai, usme se duplicates remove karke sorted tuple print karo.

numbers = (5, 1, 3, 2, 3, 5, 4, 2, 1)


unique_sorted  = tuple(sorted(set(numbers)))

print(unique_sorted)


# Tuple Reverse Karo
#  Question: Diye gaye tuple ko reverse karke print karo.

my_tuple = (1 , 2, 3, 4, 5)

reverse_tuple = my_tuple[::-1]

print(reverse_tuple)