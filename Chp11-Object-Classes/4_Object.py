# class Student: 
#     name = "Rabnawaz Dogar"




# s1 = Student()

# print(s1.name)



# # 

# class Car:
#     def __init__(self , Brand , Color):
#         self.Brand = Brand
#         self.Color = Color


#     def Show(self):
#         print(f"Brand = {self.Brand} Color = {self.Color}")




# c1 = Car("Toyota" , "Black")
# c1.Show()
# # 





class Student:
    College_name = "University of Sargodha"

    def __init__(self , Fullname , Marks , age = 20):
        self.name = Fullname
        self.Markes = Marks
        self.age = age

    def Show(self):
        print(s1.name is self.name)    

    def Get_marks(self):
        return self.Markes                                                    



s1 = Student("Rabnawaz Dogar" , 88)
print(f'Name {s1.name} ,  Marks {s1.Markes} , Age {s1.age}')
        
s1.Show()
s2 = Student("Haqnawaz Dogar" , 90)
print(f"Name {s2.name} , Marks {s2.Markes } , Age {s1.age}")

print(f"College Name {s1.College_name}")

# 
print(s1.Get_marks() , s2.Get_marks())
