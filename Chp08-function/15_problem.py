def Show_age(**info):
    if "age" in info:
        print(f"Age is =  {info['age']}")
    else:
        print("age is not provided !")


Show_age(name="Rabnawaz" , age=20)
Show_age(name="haqnawaz" , Class=10)