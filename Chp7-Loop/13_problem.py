Fruits = ["Aplle" , "Banana" , "Cherry"]
for fruits in Fruits:
    print("Fruits" , fruits)



for i in range(-1 , 11 , 2):
    print(i)




Students = {"Ali": 45 , "Ahmed" : 50 , "Asad" : 55}
 
for name , marks in Students.items():
    print(f"{name} have {marks} marks")
   
# While loop

i = 1

while i <= 5:
    print("i" , i)
    i += 1



password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access granted!")
