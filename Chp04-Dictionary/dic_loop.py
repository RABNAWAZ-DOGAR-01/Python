thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

# Value Get
for x in thisdict.values():
  print("This is a value",x)


# Key Get
for x in thisdict.keys():
  print("This is a key", x)


# Items Get
for x in thisdict.items():
  print("This is a items",x)