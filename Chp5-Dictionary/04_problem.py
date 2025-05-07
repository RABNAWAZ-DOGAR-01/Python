dict = {
    "Name" : "Rabnawaz dogar",
    "Age"  : 18,
    "Class" : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10],
    
}

dict["Name"] = "Ali"
print(dict)


# Dic_key
dict_key = dict.keys()

print(dict_key)

# Dic_values
dict_values = dict.values()
print(dict_values)

# Dict_items 

dict_items = dict.items()

print(dict_items)



# For loop

for key , value  in dict.items():
    print(f"key = {key}  value = {value} ")



# Get method

dict_get = dict.get("Name")
print("Dict Get",dict_get)


# Update method
dict.update({"hight" : 6.10 , "Names" : "Ali"})

print("Dict Update",dict)


