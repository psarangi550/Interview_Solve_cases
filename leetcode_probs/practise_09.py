# [from ast import operator


x=10
# print(x.__class__.__name__)

def fibo(num):
    a,b=0,1
    if num == 0:
        print(a)
    elif num == 1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,num+1):
            a,b=b,a+b
            print(b)

# fibo(10)

# from operator import itemgetter 
dict1={578:"Lenin Gore",901:"Angad Gupta",111:"Mark Zope"}
# dict2={k:v for k,v in sorted(dict1.items())}
# print(dict2)


# print(list1)


def foo(dict1):
    list1=list(dict1)
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[j]<list1[i]:
                list1[i],list1[j] = list1[j],list1[i]
    for item in list1:
        print(dict1[item])

    
foo(dict1)        

