list1=[205,2670,5008,500,120,30]

def foo(list1):
    result=[]
    for ele in list1:
        str_ele=str(ele)
        new_val=bar(str_ele)
        result.append(int(new_val))
    return result

def bar(str1):
    result=""
    for ele in str1:
        if ele=="0":
            continue
        else:
            result+=ele
    return result


# print(bar("205"))
print(foo(list1))


