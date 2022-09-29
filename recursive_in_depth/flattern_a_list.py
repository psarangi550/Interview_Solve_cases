list1=[[1,2],3,4,[5,6,7],[8],[9]]

result=[]
def foo(list1):
    for item in list1:
        if type(item)==list:
            foo(item)
        else:
            result.append(item)
    return result

# print(foo(list1))

print(sum([],list1))
