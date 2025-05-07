S = {1 , 2, 3, 4, 5, 6 , 7 , 8 , 9 , 10}

S.add(11)

print(S)


# Clear 
S.clear()
print(S)
print(S.clear())


# Copy 

Set_2 = {10 , 20 , 30}

Set_copy = Set_2.copy()
print("Orignal" , Set_2)
print("Set _copy",Set_copy)



# difference 

Set_D_1 = {1 , 2 , 3, 4, 5}

Set_D_2 = {6, 7 , 8, 9 ,10, 2 , 3 }

Set_diference =  Set_D_1.difference(Set_D_2)



print("Set Difference",Set_diference)




A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

A.difference_update(B)

print(A)



# Remove the specified item
Set = {1 , 2 , 3, 4 , 5}
Set.discard(2)
print("discard",Set)



# Intersections !


set_1 = {1 , 2 , 3 , 4 , 5}

set_2  = {6 , 7 , 8 , 9 , 10 , 1 ,2 , 3 , 4 , 5 , 6 , 7 , 8}

Intersections = set_1.intersection(set_2)

print(Intersections)


# isDisjiont


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)
print(z)
z_2 = x.issubset(y)
print(z_2)


# Subset 

Sub_1 = {1 , 2 , 3}

Sub_2  = { 1 , 2 , 3, 10 ,20}

Check_subset = Sub_1.issubset(Sub_2)

print("Check subset",Check_subset)




# Pop

fruits = {"apple", "banana", "cherry"}

fruits_2 = fruits.pop()

print("Pop Method",fruits_2)
print(fruits)



# Pop on empty Set

# empty_set = set()
# empty_set.pop() This Throw Erro



# Agar ek set ke saare elements ek ek karke remove karne hain, toh while loop ka use kar sakte hain.

fruits = {"apple" , "banana" , "cherrey"}

while fruits:
    print("remove pop" , fruits.pop())

    print("Final Set:", fruits)



my_set = set()

if my_set:
    print(my_set.pop())
else:
    print("Set is empty, nothing to remove!")













# Update Method in Set

Set_1 = {1 , 2 ,3 ,4 , 5}

Set_2 = {6 ,7 ,8 ,9  , 10}

Set_1.update(set_2)

print(Set_1 , set_2)




set = set()                                                  

print(type(set))