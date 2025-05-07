numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 6 , 7 , 7, 7)

user_input = int(input("Enter a number: "))

count = numbers_tuple.count(user_input)


if count > 0:
    index = numbers_tuple.index(user_input)
    print(f"Index of {user_input} : {count} times")
    print(f"First index of {user_input} :  index  = {index}")

else:
    print(f"{user_input} not found in tuple")

