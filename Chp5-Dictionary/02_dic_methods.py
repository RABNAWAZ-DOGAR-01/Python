marks = {
    "Rabnawaz dogar" : 95,
    "Haqnawaz dogar" : 99, 
    "Ali" : 80 ,
    0 : "Shohaib"
}

print(marks.items())

print("This is a keys of marks ",marks.keys())

print("This is a Values of marks" , marks.values())

marks.update({"Ali" : 85 , "Nawaab" : "100"})

print(marks)

print(marks.get("Mustafa")) # None
# print(marks["Mustafa"]) # Error

# Clear dictionary
student = {"name": "Ali", "age": 20}
student.clear()
print(student)



# dict.copy() → Dictionary Ki Copy Banana
orignal = {
  "Name" : "Rabnawaz dogar",
  "Age"  : 18,
}

dict_copy = orignal.copy()

print("this is orignal",orignal)

print("this is a copy" , dict_copy)


# dict.pop(key, default) → Key Ki Value Remove Karna
marks = {"Ali": 85, "Ahmed": 90 , "haider" : 80}

ali_marks = marks.pop("Ali")

print(marks)
print(ali_marks)

# dict.popitem() → Last (Key, Value) Pair Remove Karna
last_item = marks.popitem()

print(last_item)

print(marks)


# dict.setdefault(key, default) → Default Value Set Karna

student = {
    "Name" : "Ali",
}

student.setdefault("Age", 18)

print(student)

