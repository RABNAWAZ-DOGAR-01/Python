def function_name():
    # Function ka code
    print("Hello, ye ek function hai!")



function_name()



# Example: Function with One Parameter

def greet(name):
    print(f"Hello {name} Welcome to python!")



greet("Ali!")
greet("Rabnawaz Dogar!")



# Agar ek function ko multiple inputs chahiye, to hum multiple parameters ka use karte hain.

def Sum(a , b):
   sum = a + b
   print(f"{a} + {b} = {sum}")


Sum( 3 , 2 )
Sum(10 , 20 )


# Kabhi kabhi hume function ka result kisi variable me store karna hota hai. Iske liye hum return keyword ka use karte hain.
def Square(num):
    return num * num


result = Square(4)

print(result)



# Agar koi argument pass na kiya jaye, to hum ek default value set kar sakte hain.
def default(name= "Guest"):
    print(f"Hello {name}")



default("Ali")
default()


# Agar function me kitne arguments pass honge ye pehle se na pata ho, to hum *args ka use karte hain.
def add_numbers(*numbers):
    total_numbers = sum(numbers)
    print(f"Total sum = {total_numbers}")


add_numbers(10 , 4 , 5 , 6)
add_numbers(1 , 34 , 6)
add_numbers(89 , 328 , 8932)




#  jion String 

def jion_string(*words):
    result = " ".join(words)
    print(result)

    

jion_string("hi" , "Python" , "!")
jion_string("Hello" , "How" , "are" , "you")



#  how to Check MAX number Def 

def Max_number(*number):
    print(f"Largest number = {max(number)}")


Max_number(10 ,100 , 200 , 100)
Max_number(200 , 500 , 600)
Max_number(900 , 200 , 3200)



#  Python mein ** (Double Asterisk) Ka Matlab Function Parameters Mein
# Agar hum function ke andar **kwargs ka use karte hain (**details in this case), to iska matlab hai function named (keyword) arguments accept karega aur unko ek dictionary (dict) me store karega.


def key_value(**info):
    print(info)


key_value(name="Rabnawaz dogar" , age=19 , Class=11)





# 

def persanol_info(**detail):
    for key , value in detail.items():
        print(f"{key} , {value}")



persanol_info(name="Rabnawaz dogar" , age=19 , Class=11)

persanol_info(name="Haqnawaz Dogar" , age=15 , Class=8)


