input="A3G4B2"
output="ADGKBD"


def foo(str1):
    result=""
    for ele in str1:
        if ele.isdigit():
            result+=chr((ord(result[-1])+int(ele)))
        else:
            result+=ele
    return result

print(foo(input))


        
