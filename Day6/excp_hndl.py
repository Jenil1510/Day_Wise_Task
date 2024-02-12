#Error handling or the excepetion handling

def table(a): 
    try:
        a=int(input("Enter the number:"))
        print(f"The Table of {a} is given below")
        for i in range(1,11):
            print(f"{int(a)}x{i}={int(a)*i}")
    except ValueError:
        print("Entered number is not integer")
    
    except SyntaxError:
        print("Syntax is wrong of the program")
        
x=table(1)


        
    
