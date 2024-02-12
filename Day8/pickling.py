import pickle

#pickling the file 

# cars=["G-wagon","Porshe","Bmw","X8"]
# file="mycar.pickle"
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)

#de-pickling the file   

file="mycar.pickle"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
