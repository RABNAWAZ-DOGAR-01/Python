day = 4

match day:
    case 1:
         print("Monday")
    case 2:
          print("Tuseday")
    case 3:
          print("Wednesday")
    case 4:
          print("thursday") 
    case 5:
          ("Friday")
    case 6:
            print("Sturday") 
    case 7:
            print("Suunday")


def Switch_Case(Value):
      cases = {
            1 : "One",
            2 : "Tow",
            3 : "Three"

      }


      return cases.get(Value , "Invalid")

print(Switch_Case(2))
print(Switch_Case(1))



Value = 4


match Value:
    case 1:
        print("One")
    case 2:
            print("Tow")
    case 3:
            print("Three")
    case 4:
            print("Four")



