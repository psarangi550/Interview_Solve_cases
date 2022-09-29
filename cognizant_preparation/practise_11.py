str1="abcaba"

def foo(str1):
    dict1={}
    result=""
    for ele in str1:
        if ele not in dict1:
            dict1[ele]=1
            result+=dict1[ele]*ele
        else:
            dict1[ele]+=1
            result+=dict1[ele]*ele
    print(result)

foo(str1)
        
