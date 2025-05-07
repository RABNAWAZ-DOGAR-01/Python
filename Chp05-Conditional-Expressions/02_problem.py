marks_1 = int(input("Enter Marks 1 :"))
marks_2 = int(input("Enter Marks 2 :"))
marks_3 = int(input("Enter Marks 3 :"))


# Check for total percentage
total_percentage = (100*(marks_1 + marks_2 + marks_3))/300

if (total_percentage>=40 and marks_1>=33 and marks_2>=33 and marks_3>=33):
    print("You are pass", total_percentage)

else:
    print("You failed")