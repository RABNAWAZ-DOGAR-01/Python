def login():
    user = {"admin": "1234", "user": "pass"}

    try:
        username = input("Enter username: ")
        password = input("Enter passwors: ")

        if username in user:
            if user[username] == password:
                print("login successful!")
            else:
                print("Invalid password!")
        else:
            print("Invalid username!")
    except ValueError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



login()

            


    