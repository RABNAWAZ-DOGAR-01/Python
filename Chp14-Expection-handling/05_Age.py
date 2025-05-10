def ZeroDivision(a , b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Invalid input! Please enter numbers.")
    except ValueError:
        print("Invalid input! Please enter numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of {a} / {b} = {result}")
    finally:
        print("Execution completed.")



ZeroDivision(10 , 0)
ZeroDivision(10 ,3)
ZeroDivision(10 , "a")
    


    

        

