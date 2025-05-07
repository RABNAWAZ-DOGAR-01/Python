class Student:
    def __init__(self , Name , Marks):
        self.Name = Name
        self.Marks = Marks




    def get_Marks_avg(self):
        sum = 0
        for value in self.Marks:
            sum += value
            print(f"hi {self.Name} your Marks average is {sum/3}")


    @staticmethod
    def get_hello():
        print("Hello")

        






s1 = Student("Rabnawaz Dogar" ,[10 , 20 , 30 , 40])
s1.get_Marks_avg()
s1.get_hello()