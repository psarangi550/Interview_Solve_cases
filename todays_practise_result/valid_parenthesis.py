#valid brackets 
s=")("

def foo(str1):
    list1=[]
    list2=["(","{","["]
    dict1={
        "(":")",
        "{":"}",
        "[":"]"
        }
    for ele in str1:
        if ele in list2:
            list1.append(ele)
        else:
            if list1:
                item=list1.pop()
                if dict1[item]!=ele:
                    return False
                else:
                    continue
            else:
                return False
    return True

print(foo(s))

