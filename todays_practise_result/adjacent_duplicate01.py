str1="abbaca"
# str1="azxxzy"

list2=[]

def foo(str1):
    for ele in str1:
        if ele not in list2:
            list2.append(ele)
        else:
            if list2:
                item=list2.pop() #b
                if item==ele:
                    continue
    return "".join(list2)

#using the recursive approach
str1="abbaca"
result=""
def bar(str1):
    global result
    if len(str1)==0:
        return result
    else:
        if str1[0]!=str1[1]:
            result+=str1[0] #a
        else:
            str1=str1[1:]
    return foo(str1[1:])


            
# print(list2)
# print(foo(str1))
print(bar(str1))
print(result)



#alternate approach for removing adjacent elements
list1=[]
def foo(str1):
    for ele in str1:
        if list1 and list1[-1]==ele:
            list1.pop()
        else:
            list1.append(ele)
    return "".join(list1)

print(foo("abbaca"))
