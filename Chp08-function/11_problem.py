def rem(l , Word):
    for item in l:
        l.remove(Word)
        return l
        


l = ["Rabnawaz" , "haqnawaz" , "Sadiq"]
      

print(rem( l , "Rabnawaz"))





def rem(l , Word):
    n = []
    for item in l:
        if not(item == Word):
            n.append(item.strip(Word))
            return n
       
        


l = ["Rabnawaz" , "haqnawaz" , "Sadiq" , "Alinawaz" , ]
      

print(rem( l , "awaz"))
