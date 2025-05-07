# Frozan Set home work ha


my_set = {5 , 4 , 3 ,2 , 1}

print(my_set)


empty_set = set()

print(type(empty_set))


# Set Me Values Access Karna
# Kyuki set unordered hota hai, isme indexing nahi hoti!
# Matlab my_set[0] likhne se error aayega.
# Lekin loop ya type conversion se values access kar sakte ho.

my_set = {10 , 20 , 30 , 40 ,50}
sorteds  =  sorted(my_set)
for item in sorteds:
    print(item)


# add() – Set me ek element add karne ke liye
my_set = {10 ,20}
my_set.add(30)
print("Add",my_set)

# Remove
my_set.remove(10)
print("Remove",my_set)


# Discard
my_set.discard(330)
print("Discrab",my_set)


# Clear 
my_set.clear()
print("clear",my_set)


# union() – Do sets ko mila ke ek naya set banaata hai
set_1 = {1 , 2 , 3 ,4 , 5  , 1 , 2 }
set_2 = {6 , 7 , 8 , 9 ,10 , 6 , 4 , 1 ,2}

result = set_1.union(set_2)

print("Union",result)


# intersection() – Sirf common elements return karta hai

result2 = set_1.intersection(set_2)

print("Intersection",result2)



# issubset() – Check karta hai ke ek set doosre me included hai ya nahi
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True





# difference() – Ek set me jo elements hain par doosre me nahi

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff = set1.difference(set2)
print(diff)  # Output: {1, 2}


# issuperset() – Check karta hai ke ek set doosre ko contain karta hai ya nahi
set1 = {1, 2, 3, 4, 5}
set2 = {1 , 4}
print(set1.issuperset(set2))  # Output: True



s = set()
s.add("20")
s.add(20)
s.add(20.0)

print(s)
print(len(s))