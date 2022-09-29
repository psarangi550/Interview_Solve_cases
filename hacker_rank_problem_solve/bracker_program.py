def foo(str1):
    list2=[]
    list1=["{","(","["]
    dict1={"{":"}","(":")","[":"]"}
    for ele in str1:
        if ele in list1:
            list2.append(ele)
        else:
            if list2:
                e=list2.pop()
                if dict1[e]!=ele:
                    return False
                else:
                    continue
            else:
                return False
    return True

print(foo("(){}[)"))

