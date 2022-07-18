from collections.abc import Hashable

tup1=(10,20,30)
print(hash(tup1))
print(isinstance(tup1,Hashable))

dict5={"eno":100,"ename":"rika"}
dict6=dict5={"eno":100,"ename":"rika","esal":5000}

print(dict5==dict6)

dict1={"roll":101,"name":"rika"}
dict2={"addr":"bangalore"}

print("The Name of Student is {name} and Roll Number is {roll}".format(**dict1))

print(dict1.items())
print(dict1.keys())

dict3={x:x**x for x in range(1,6)}
print(dict3)