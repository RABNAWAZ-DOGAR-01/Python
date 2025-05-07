# List ke andar Tuples
students = ("Ali", 20, "Zain", 2,["Hassan", 21])

# Accessing Tuple Data
print(students[4][0])


# List ke andar Tuples
students = [("Ali", 20), ("Zain", 22), ("Hassan", 21)]

# Accessing Tuple Data
print(students[0])  # Output: ('Ali', 20)
print(students[1][1])  # Output: 22



#  Set ke andar Tuples

Set_tuple = {(1,2) , (3,4) , (1,2)}

print(Set_tuple)



# Tuples in Dictionaries

Tuple_d = {("Ali" , "Math"):90 , ("hassan" , "Scince"):50}

print(Tuple_d[("Ali" , "Math")])



# Max or minimum

Tuple = (10 , 20 , 4 , 50)

max_tuple = max(Tuple)
print(max_tuple)
min_tuple = min(Tuple)
print(min_tuple)

Tuple_reverse = Tuple[::-1]
print("Tuple Reverse" , Tuple_reverse)