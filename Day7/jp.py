from abc import ABC,abstractclassmethod

class Animal(ABC):
        # """move() works by first creating a copy of the file with the path defined by old_path and storing the copy in the new location, new_path """
    @abstractclassmethod
    def move(self):
        print("hey")
    
class human(Animal):
    def move(self):
        print("I can walk")
        
class snake(Animal):
    def move(self):
        print("i cant walk")
        

a=human()
print(a.move())
