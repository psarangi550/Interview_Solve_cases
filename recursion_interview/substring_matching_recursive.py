def func(str1,str2):
    size1=len(str1)
    size2=len(str2)
    if size1==0:
        return False
    if size2==0:
        return True
    if(str1[0]==str2[0]):
        return ExecuteFunc(str1,str2)
    return func(str1[1:],str2)

def ExecuteFunc(str1,str2):
    size1=len(str1)
    size2=len(str2)
    if size1==0:
        return False
    if size2==0:
        return True
    if (str1[0]==str2[0]):
        return ExecuteFunc(str1[1:],str2[1:])
    else:
        return False

    

print(func("NETSETOS","SET"))
