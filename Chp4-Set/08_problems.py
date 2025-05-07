my_set = set()


user_input = input("Enter the number :").strip()


if user_input:
    my_set.update(map(int , user_input.split(",")))

print(my_set)
