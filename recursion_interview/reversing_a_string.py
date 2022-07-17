# list1=[10,30,40,20,50]
# list1.sort()
# print(list1)


#reversing a string using the recursion
letter="NETSETOS"

# def func(str_letter):    
#     size=len(str_letter)
#     if size==0:
#         print("")
#     else:
#         print(str_letter[-1],end="")
#     func(str_letter[:-1])

# output=func(letter)
# print(output)

result=[]
def func(str_letter):    
    size=len(str_letter)
    if size==0:
        return 
    else:
        result.append(str_letter[-1])
    return func(str_letter[:-1])

func(letter)
print("".join(result))



