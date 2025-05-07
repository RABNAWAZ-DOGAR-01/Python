class Student:
    Collage_name = "University of Sargodha"
            
    def __init__(self , FullName , Marks = 10):
        self.Name = FullName
        self.Age = 20
        self.Marks = Marks
        print("This is a constructor")

    
    def Welcome(self):
        print("Welcome to the class" , self.Name)



    def get_Marks(self):
        return self.Marks




s1 = Student("Rabnawaz Dogar")
print(f' Name = {s1.Name } Age = {s1.Age}  Marks = {s1.Marks} ')


s2 = Student("Haqnawaz Dogar")
print(s2.Name)

print(s1.Collage_name)

s1.Welcome()


print(s1.get_Marks())