print(1)
print(2)
print(3)
print(4)
print(5)


# The same task can done like this !
for i in range(1, 201):
    print("this loops",i)

sum = 0
for num in range(1, 101):
    sum += num
print("Total Sum:", sum)




fruits = ["apple" , "banana" , "cherry"]

for fruits in fruits :
    print("Fruits", fruits)



x = 1

while x <= 5:
    print("x" , x)
    x += 1


for num in range(1, 10):
    if num == 5 :
        break
    print("Break",num)


for num in range(5):
 if num == 2:
     continue
 print(num)
       