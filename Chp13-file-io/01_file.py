import json

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close



# file = open("file.txt")

# content = file.read()

# print(content)

# file.close




#  

file = open("file.txt")

for line in file:
    print("Line" , line.strip())

file.close()



# 

with open("file.txt" , "a") as file:
 content  =    file.write(" Hi Rabnawaz ")
print(content)


# 
data = {
   "Name" : "Rabnawaz",
   "Age"  :  20,
   "Country" : "Pakistan"
}


with open("data.json" , "w") as f:
   json.dump(data , f)




with open("data.json" , "r") as file:
   data = json.load(file)
   print(data)



# 

name = input("Enter your name : ")
age = input("Enter your age : ")
Country = input("Enter your Countery Were are From ")


user_data = {
   "Name" : name ,
   "Age"  : age ,
   "Country" : Country
 }


with open("user_data.json" , "w") as f:
   json.dump(user_data , f)
   print("✅ Data saved to 'user_data.json' file successfully!")


with open("user_data.json" , "r") as f:
   data = json.load(f)
   print(data)

