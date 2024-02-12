# https://wiki.python.org/moin/Decorators

# https://www.geeksforgeeks.org/top-python-built-in-decorators-that-optimize-python-code-significantly/

# implementing the builtin decorators in python 

# 1.@lassmethod for boundingparticular class

class decorator_built_in1:
    var=10
    
    @classmethod
    def class_mthd(cls):
        print("The clas smethod is called")
        print(f"The value of class variable is:{cls.var}")
    
decorator_built_in1.class_mthd()

import atexit
class decorator_built_in2:
    
    @atexit.register
    
    def message():
        print("Bye friends")
        
print("Hey Friends")

decorator_built_in2()

from enum import Enum, unique
class decorator_built_in3:
    
    @unique
    def Days():
        MONDAY=1
        TUESDAY=2
        WEDNESDAY=3
        THURSDAY=2
        
# decorator_built_in3.Days()