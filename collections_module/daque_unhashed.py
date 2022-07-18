from collections import deque
#importing the daque from the collections module 
list1=[10,20,30,40,50]
dq=deque(list1)
dq.rotate(1)
print(dq.maxlen)
