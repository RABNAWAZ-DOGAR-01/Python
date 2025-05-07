Dictonery = {
    "Car" : "4x4",
    "Model" : "Toyota",
    "Year" : 1999,
}


Dictonery["Year"] =  2000
print(Dictonery) # {'Car': '4x4', 'Model': 'Toyota', 'Year': 2000}


Dictonery.update({"Year" : 2001 , "Color" : "black"})
print(Dictonery)

# pop method randomly pop the item from the dictonery
Dictonery.popitem()
print(Dictonery)



# The del keyword removes the item with the specified key name:

del Dictonery["Model"]
print(Dictonery)




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
