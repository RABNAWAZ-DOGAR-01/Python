t = (1, 3, 5, 3, 7, 3, 5, 5, 5, 7,7)


Most_common = max(set(t), key=t.count)

print(Most_common)




# Merge Two Tuples Without Using + Operator
# 👉 Given two tuples, merge them into one.

t1 = (1 , 2 ,3)

t2 = (4 , 5 ,6)

marge_tuple = (*t1 , *t2)

print(marge_tuple)



list_of_tuples = [(1 , 2 , 3 , 10) , (4, 5 , 6 , 20) , (7 , 8 , 9 , 40)]


max_tuple = max(list_of_tuples , key=lambda t: sum(t))

print("Max tuples",max_tuple)


temp_list = list(list_of_tuples[1])

temp_list[2] = 100

print("Updated tuple",(temp_list) , type(temp_list), type(list_of_tuples[1]))
