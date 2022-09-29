def beautiful_day(start,end,num):
    count=0
    for i in range(start,end+1):
        str_num_val=str(i)
        rev_num=int(str_num_val[::-1])
        if abs(i-rev_num)%num==0:
            count+=1
    return count

print(beautiful_day(20,23,6))
