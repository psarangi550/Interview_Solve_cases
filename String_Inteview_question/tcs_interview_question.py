
str1 = "elementmanager"

index = 0


def func(str1):
    global index
    if str1.count("e") == 1:
        return str1
    else:
        index = str1.index("e")
        str1 = str1[index+1:]
    return func(str1)


print(func(str1))
