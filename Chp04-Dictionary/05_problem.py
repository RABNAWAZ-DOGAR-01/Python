dict = {
    "Name" : "Rabnawaz dogar",
    "Age"  : 18,
    "Class" : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10],
    "option" : {1 : "one" , 2 : "two" , 3 : "three"},
    "Tuple" : (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10)
}



dict_get = dict.get("Class")

dict_get_index_list = dict_get[7]


print(dict_get_index_list)


dict_get_index_dict = dict.get("option")

dict_get_index_dict_value = dict_get_index_dict[2]

print(dict_get_index_dict_value)




# tuple = dict.get("Tuple")
# print(type(tuple))
# tuple_index = tuple[5]

# tuple_index_change = tuple_index = 12
# # tuple_convert_list = list(tuple)
# print(tuple)
# print(tuple_index_change)


tuple_list = list(dict.get("Tuple"))

tuple_list[5] =  12
tuple_list.remove(1)
tuple_convert_tuple = tuple(tuple_list)
tuple_index_getting = tuple_convert_tuple[2]
print((tuple_index_getting))
print(sorted(tuple_convert_tuple))
print(tuple_convert_tuple.count(4))