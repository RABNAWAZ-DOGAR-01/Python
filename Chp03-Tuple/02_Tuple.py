# Tuple vs List (Key Differences)
# Feature	Tuple (tuple)	List (list)
# Mutability	Immutable	Mutable
# Speed	Faster	Slower
# Memory Usage	Less	More
# Methods	Limited (count, index)	Many (append, remove, etc.)
# Use Case	Fixed collections	Dynamic collections


my_dict = {(1,2) : "Rabnawaz dogar"}
print(my_dict[(1,2)])


# Converting Between Tuples and Lists
# 1. Tuple to List



# 1. Converting Between Tuples and Lists
my_tuple = (1,2,3)

my_list = list(my_tuple)

print(my_list)





# 2. List to Tuple
my_tupel_2 = tuple(my_list)

print(my_tupel_2)



# Nested Tuples
# Tuples can contain other tuples.

nested_tuple = ((1 , 2) , (3 , 4) , (5 , 6))
print(nested_tuple[0])
print(nested_tuple[1][1])



# 4. Swapping Two Variables

a , b = 5 , 10

a , b = b , a

print("A",a ,"B", b)



# Iterating Over Tuples in a for Loop
Student = [("Rabnawaz" , 19) , ("Sadiq" , 40) , ("haqnawaz" , 16)]

for Name , Age in Student :
    print(f"Name : {Name} , Age : {Age} ")



# Tuples in enumerate() for Indexing

Colors = ("Red" , "Blue" , "white")

for index , Colors in enumerate(Colors):
    print(f"Colors {index} {Colors}")


# Tuples can be used to pass multiple arguments to a function.
def add(x , y , z):
    return(x + y + z)

Numbers = (2  , 3 , 5)
result = add(*Numbers)

print(result)