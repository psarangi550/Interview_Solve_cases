def func(str1,str2):
    
    if len(str1)==0:
        return False
    if len(str2)==0:
        return True
    if str1[0]==str2[0]:
        return CheckMatch(str1,str2)
    return func(str1[1:],str2)
    

def CheckMatch(str1,str2):
    if len(str1)==0:
        return False
    if len(str2)==0:
        return True
    if str1[0]==str2[0]:
        return CheckMatch(str1[1:],str2[1:])
    else:
        return False

val=func("NETSETOS","SET")
print(val)