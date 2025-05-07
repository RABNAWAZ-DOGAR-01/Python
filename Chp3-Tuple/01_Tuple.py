# Tuples are created using parentheses () or the tuple() function.
# 1. Using Parentheses
my_tuple = (1 , 2 , 3 , 4 , 5)

print(my_tuple)
print(type(my_tuple))


# 2. Without Parentheses (Implicit Tuple)# Parentheses are optional
my_tuple = 1, 2, 3, 4
print(my_tuple)  


# 3. Using the tuple() Constructor
my_tuple = tuple([10 , 20 , 30])
print(my_tuple)
print(type(my_tuple))


# 4. Creating a Tuple with a Single Element
# For a single-element tuple, add a trailing comma; otherwise, Python treats it as a normal value.
single_element_tuple = (5,)

print(type(single_element_tuple))


not_a_tuple = (5)
print(type(not_a_tuple))



# Accessing Tuple Elements
# 1. Indexing
# Tuples support zero-based indexing to access individual elements.

my_tuple = ("apple" , "banana" , "grapes")
print(my_tuple[0])
print(my_tuple[2])


# 2. Negative Indexing
print(my_tuple[-1])
print(my_tuple[-2])


# 3. Slicing Tuples
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # output 20 30 40
print(my_tuple[:3])   # output 10 20 30
print(my_tuple[2:])  # output 30 40 50
print(my_tuple[-3:-1])  # output 30 40


# Tuple Methods
# Since tuples are immutable, they have only two built-in methods:
# count()
# index()


my_tuple = [1 , 2 , 3, 4 , 5 , 6 , 7 , 1 , 1 , 1]
print(my_tuple.count(1))

# index
print(my_tuple.index(7))


# Tuple Operations
# 1. Tuple Concatenation (+)
tuple_1 = (1 , 2 , 3 , 4 , 5)
tuple_2 = (6 , 7 , 8  , 9 , 10)
Concatenation = tuple_1 + tuple_2
print(Concatenation)



# 2. Tuple Repetition (*)
Result = tuple_1 * 3
print(Result)


# 3. Checking Membership (in, not in)
my_tuple = ("apple" , "banana" , "orange")
print("apple" in my_tuple)
print("grapes" is not my_tuple)



# Tuple Unpacking
# Tuple unpacking allows assigning values from a tuple to multiple variables at once.
a , b , c = my_tuple
print(a , b , c)