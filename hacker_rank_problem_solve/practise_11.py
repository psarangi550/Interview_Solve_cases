list1=[4,4,1,3]

#using the max function

# def foo(list1):
#     count=0
#     max_digit=max(list1)
#     for i in list1:
#         if i==max_digit:
#             count+=1
#     return count

# print(foo(list1))

#WITHOUT USING THE MAX FUNCTION


def max_num(list1):
    max=list1[0]
    for ele in list1:
        if ele>max:
            max=ele
    return max

def bar(list1):
    max=max_num(list1)
    count=0
    for ele in list1:
        if ele==max:
            count+=1
    return count

print(bar(list1))
            
        
    
