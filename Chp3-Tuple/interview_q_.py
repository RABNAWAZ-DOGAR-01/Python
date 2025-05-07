paris = (("Name" , "Alice") , ("Age" , 20) , ("City" , "Newyork"))


# Convert tuple to dictionary
result = dict(paris)


print("convert to dict",dict(paris))
print("Paris type",type(result))



#  Dictionary to Tuple Conversion
# 📌 1️⃣ Keys ko Tuple me Convert Karna


d = {"Name" : "Alice" , "Age" : 20 , "City" : "Newyork"}

result = tuple(d.items())

print(type(result),result)

# Set ko direct tuple me convert kar sakte hain using tuple().

s = {1 , 2, 3, 4 , 5}

result = tuple(s)

print("Set",result , type(result))




# List ko direct tuple me convert kar sakte hain using tuple().
l = [1, 2, 3, 4, 5]
result = tuple(l)
print("List",result , type(result), "This is original list" , l)  

# Output: (1, 2, 3, 4, 5)




# Agar tuple ko wapas kisi aur data type me convert karna ho, to yeh tareeqe hain:
t = (10, 20, 30)
list_from_tuple = list(t)
print(list_from_tuple)  
# Output: [10, 20, 30]




t = (10, 20, 30, 10)
set_from_tuple = set(t)
print(set_from_tuple)  
# Output: {10, 20, 30}  (Duplicates remove ho jayenge)
