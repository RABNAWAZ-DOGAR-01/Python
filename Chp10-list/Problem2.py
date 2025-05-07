# Dictionary Ke Andar List:

Student = {
     "name": "Ali",
    "age": 22,
    "subjects": ["Math", "Physics", "Python"]
}

print(Student["subjects"][1])



# List Ke Andar Dictionaries:
Students = [
    {"name" : "Ali" , "age" : 22},
    {"name" : "sara" , "age" : 19}
]

print(Students[1]["name"])


# Hum list ko set mein convert kar sakte hain taake duplicate values hat jaayein:
l = [ 1 , 2 , 1 ,2 , 1 , 3  ,4 , 5 , 5 , 6 ,7]

s = set(l)

print(list(s))



# 
l = []
l.append("Rabnawaz")
print(l)



shopping_cart = [
    {"product": "T-Shirt", "price": 1000, "quantity": 2},
    {"product": "Shoes", "price": 3000, "quantity": 1},
    {"product": "Watch", "price": 1500, "quantity": 1}
]


print(shopping_cart[0]["product"])
print(type(shopping_cart[1]["price"]))
print(type(shopping_cart[0]["price"]))




total_price = sum(item ["price"] * item["quantity"] for item in shopping_cart)


print("this is a total price",total_price)