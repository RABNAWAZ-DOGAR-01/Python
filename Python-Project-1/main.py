import random

'''
1 for Sanke 
-1 for Water
0 for gun
'''


computer = random.choice([-1 , 0 ,1])

youserStr = input("Enter your choice:")

youDict = {"s" : 1 , "w" : -1 , "g" : 0}

reversdict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}

you = youDict[youserStr]


print(f"You choice is {reversdict[you]}\nCoumputer choice is {reversdict[computer]}")


if computer == you :
    print("Match Draw")


else:
    if(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You Win")
    elif(computer == 0 and you -1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose")

    else:
        print("Invalid input")


    
    
