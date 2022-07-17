
def func(n):
    i=0
    while i < n:
        yield i
        i+=1

def isprime(num):
    for n in range(2,num):  
        if (num % n) == 0:  
            return False
    return True
    
# print(isprime(55))

output=func(100)
for ele in output:
    result=isprime(ele)
    if result:
        print(ele)
    else:
        continue
    

# def func(mystr):
#     new_str=""
#     for i in range(len(mystr)):
#         if i ==0 or i==3:
#             new_str+=mystr[i].capitalize()
#         else:
#             new_str+=mystr[i]
#     return new_str

# print(func("pratikkumar"))


