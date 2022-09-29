def prisioner_candy(pr_no,candy,start):
    for i in range(start,pr_no+1):
        candy-=1 
        if candy==0:
            return i
        if i==pr_no:
            return prisioner_candy(pr_no, candy,1)
        
        

print(prisioner_candy(5,2,1))
print(prisioner_candy(5,2,2))
print(prisioner_candy(4,6,2))
print(prisioner_candy(7,19,2))
print(prisioner_candy(3,7,3))


