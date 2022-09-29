str1="abc,abcd,abcdgff,dfr,d,ser"
output="abc,abc,d,abc,dg,dfr,d,ser"

result=[]
def foo(str1):
    global result
    list1=str1.split(",")
    for index,ele in enumerate(list1):
        if len(ele)>3:
            first=ele[:3]
            second=ele[3:]
            result.insert(index,first)
            result.insert(index+1,second)
            if len(second)>3:
                foo(second)
            else:
                continue
        else:
            result.append(ele)
    return result

print(foo(str1))