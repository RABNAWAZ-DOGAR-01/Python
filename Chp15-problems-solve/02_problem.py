Fruits = {
    "banana" : 100 ,
    "Apple" : 150 , 
    "Orange" : 230 ,
    "grapes" : 500 , 
}

Fruits_names = list(Fruits.keys())
Fruits_price = tuple(Fruits.values())
unqiue_price = set(Fruits_price)


print("Fruits List :" , Fruits_names)
print("Fruits Tuple :" , Fruits_price)
print("Fruits Unqiue price :" , sorted(unqiue_price))