# Returns the index of the first occurrence of a substring; -1 if not found.
Name = "Rabnawaz Dogar"
print(Name.find("Dogar"))
# Result 9

# Returns the last occurrence of a substring.
print(Name.rfind("Rabnawaz"))
# Result 0


# Counts occurrences of a substring.
Fruits = "Bananana"
print(Fruits.count("a"))
# Result 4



# Replaces occurrences of a substring.
Name_1 = "Rabnawaz Dogar"
Name_2 = Name_1.replace("Rabnawaz Dogar","Haqnawaz Dogar")
print(Name_2)


# 2. Replace only the first few occurrences
text = "apple banana apple orange apple"
new_text = text.replace("apple", "grape", 2)
print(new_text)


#  Removing a substring
text = "I love Python programming!"
new_text = text.replace("Python ", "")
print(new_text)



