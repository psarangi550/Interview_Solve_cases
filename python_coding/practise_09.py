# Input_s = "()"

s = "()[]{}"

#Output: True
dict1={
    '{':"}",
    '(':")",
    "[":"]"
    }

list1=["{","[","("]

def foo(str1):
    stack=[]
    for ele in str1:
        if ele in list1:
            stack.append(ele)
        else:
            if len(stack) !=0 :
                top=stack.pop()
                if dict1[top]!=ele:
                    return False
                else:
                    continue
            else:
                return False
    return True

print(foo(s))