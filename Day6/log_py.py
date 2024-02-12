import logging

a=int(input("Enter the value between 1 to 20 or 41 to 50:"))
if(a>20 and a<40):
    logging.error(f"you enter {a} which is>20 and <40 ")
elif(a>50):
    logging.warning("You are going out of bound")
else:
    print(a)


