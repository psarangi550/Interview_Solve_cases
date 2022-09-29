str1="TANUJ"

def func(str1):
    for i in range(len(str1)):
        for j in range(i+1):
            print(str1[j],end=" ")
        print()

def new_func(str1):
    if len(str1)==0:
        return
    else:
        func(str1)
    return new_func(str1[1:])

new_func(str1)
