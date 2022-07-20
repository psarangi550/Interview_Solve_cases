import itertools
from itertools import repeat
from itertools import starmap
#itertools.count() #this will return an iterator which can go to infinity number 
#starts from 0 and tun till infinity 
# list1=[100,200,300,400]
# iter_list=zip(itertools.count(),list1)
# list2=list(iter_list)
# print(list2)

# li1=list(map(pow,[x for x in range(10)],itertools.repeat(2)))
# print(li1)

# #usage of start map
# li2=list(starmap(pow,zip(range(10),itertools.repeat(2))))
# print(li2)

# from itertools import islice
# with open("text.txt","r")as f:
#     datas=islice(f,1,100)
#     for data in datas:
#         print(data)

# from itertools import accumulate
# iter_fibo=accumulate(range(100))

# for val in iter_fibo:
#     print(val)


from itertools import groupby,tee
iter_list=tee([10,20,30,40,50],3)
for val in iter_list:
    print(list(val))

