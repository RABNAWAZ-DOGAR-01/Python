class Student:
    def __init__(self , Name , Marks ):
        self.Name = Name
        self.Marks = Marks


    def Avg(self):
        sum = 0
        for val in self.Marks:
            sum += val
        print(f"hi {self.Name} your Average Score is {sum/3}")

    @staticmethod
    def Hello():
        print("Hello World!")


s1 = Student("Rabnawaz Dogar" , [20 , 40 ,50])
s1.Name = "Haqnawaz Dogar"
s1.Avg()

s1.Hello()