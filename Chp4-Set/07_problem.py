text = "Apple , Banana , Cherry"

fruits = text.split(",")


print(fruits)


sentence = "Paython is amazing"

words = sentence.split(" ")

print(words)



sentence_2 = "   Python is Top lanuage in world       "


Word = sentence_2.split()

print(Word)

print("Word",type(Word))


# strip() + split() Together (Best Use Case)
# Agar user comma-separated numbers enter kare, toh split() unko list me badal dega, lekin strip() har number ke aas paas ke extra spaces remove karega.


user_input = "  10,  20,30 ,  40 ,50  "  # Input with extra spaces

# Strip aur split ek sath use karna
numbers = list(map(int, map(str.strip, user_input.split(","))))

print(numbers)
