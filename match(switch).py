day = input ("enter number :")
match int(day):
      
         case 1|2|3|4|5:
            print("Working day")
         case 6|7:
                    print("Funday")
         case _:
            print("Invalid day")
            print("Please enter a number between 1 and 7")