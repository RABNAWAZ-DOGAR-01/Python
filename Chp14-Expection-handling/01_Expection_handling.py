# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("Execution completed.")




try:
    x = int(input("Enter a number: "))
    Result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {Result}")
finally:
    print("Execution completed.")


print("\n=========\n")


try:
    val = int(input("Enter number: "))
    print(10 / val)
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)



class MyError(Exception):
    pass

try:
    raise MyError("This is a custom error message.")
except MyError as e:
    print("Caught MyError:", e)