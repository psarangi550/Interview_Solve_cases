# a=[2,6]
# b=[24,36]
a=[2,3]
b=[2,4]
i=2
result=[]
def foo(n1,n2):
    global i
    global result
    if n1>n2:
        if i>n2:
            return result
        elif n1%i==0 and n2%i==0:
            result.append(i)
    if n2>n1:
        if i>n1:
            return result
        elif n1%i==0 and n2%i==0:
            result.append(i)
    i+=1
    return foo(n1,n2)

foo(2,4)
print(result)


# def bar():
#     val=foo(2,4)
#     for ele in val:
#         if ele%a[0]==0 and ele%a[1]==0:
#                 print(ele)
#         else:
#             continue
# bar()
        

