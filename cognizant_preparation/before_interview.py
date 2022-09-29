
list1=[2,17,6,8,1]

def foo(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[j]>list1[i]:
                break
        else:
            print(list1[i])

foo(list1)