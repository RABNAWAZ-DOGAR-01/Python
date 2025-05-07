Students = {
    "Ali": 85,
    "Sara": 92,
    "Hassan": 38,
    "Fatima": 77,
    "Zain": 29
}


top_score = max(Students , key=Students.get)

top_marks = Students[top_score]

Faild_studets = {name for name , marks in Students.items() if marks < 50}

print(f"Top Student is {top_score} with {top_marks} marks")
print("Faild Students are:", Faild_studets)