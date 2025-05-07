# User input
list_1 = set(map(int , input("Enter first list: ").split(",")))
list_2 = set(map(int , input("Enter second lsit:").split(",")))


# Find common and unique elements
comman_elements = tuple(list_1 & list_2)
unqiue_dict = {"List1 Unique": list_1 - list_2 , "List1 Unique": list_2 - list_1}


print("Common Elements (Tuple):", comman_elements)
print("Unique Elements Dictionary:", unqiue_dict)