def greet():
    print("Hello, Welcome to Python!")

greet()  # Function call




def add(a,b):
    return a+b


result = add(10,20)

print(result)


# Agar tum function me values pass karna chahte ho, toh parameters ka use hota hai.

def greet(name):
    print(f"Hello , {name}")




greet("Rabnawaz")
greet("Haqnawaz")




def multiply(a,b):
    return a*b

result = multiply(10,20)


print(result)


# Agar tum function ko bina kisi argument ke bhi call karna chahte ho, toh default parameter use kar sakte ho.

def greet(name="Guest"):
    print(f"Hello , {name}")


greet("Rabnawaz")
greet()



# Agar function koi value return karna chahta hai, toh return keyword ka use hota hai.

def sqaure(n):
    return n *  n


print(f"Sqaure{sqaure(10)}")


# Agar tumhe exact number of parameters nahi pata, toh *args ka use hota hai.


def add_numbers(a , b , *args):
    return sum(args)

print("Total sum",add_numbers(10,20,39,49,50,60))
print("Total sum",add_numbers(10,20,39,49,50,60,70,80,90,100))


# Agar tum keyword-value pair pass karna chahte ho, toh **kwargs ka use hota hai.

def student_info(**details):
    for key , value in details.items():
        print(f"{key} = {value}")

student_info(name="Rabnawaz" , age= 20 , country="Pakistan")



# Function ka ander dictonery 

def student_details():
    student_d = {
        "name" : "Rabawaz",
        "age" : 19,
        "country" : "pakistan"
    }
    for key , value in student_d.items():
        print(f"{key} = {value}")
 


student_details()



# Agar tum dictionary ko function se wapas return karwana chahte ho, toh return ka use karo:

def greet():
     student_d_ = {
        "name" : "Rabawaz",
        "age" : 196,
        "country" : "pakistan"
    }
     return student_d_




student_info = greet()

print(student_info)
     
    




