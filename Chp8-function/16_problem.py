def student_info(**details):
    name = details.get("name" , "Unknown")
    age = details.get("age" , "Age is not provided")
    print(f"Name = {name} Age = {age}")



student_info(name="Rabnawaz" , age = 20)