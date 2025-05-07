def Menu(option):
    match option:
        case "1":
            print("You selected Login")
        case "2":
            print("You selected Signup")
        case "3":
            print("You selected Exit")
        case _:
            print("Invalid option")



Menu("2")
    