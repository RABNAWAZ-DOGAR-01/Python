def numbers(a , b , *args , d=10 , **Args):
    print(f"A : {a} B : {b}")
    print(f"Args : {args}")
    print(f"D : {d}")
    print(f"Args : {Args}")



numbers(10 , 20 , 30 , 40 , 50 , 60 , d = 20 , k = 100 , y = 99)