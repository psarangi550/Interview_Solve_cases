list1=[1,-1,3,7,8,0,2,5,10]
requ_val=[1,2,3,4,5,6,7,8,9]

for val in requ_val:
    if val not in list1:
        print(val)
        break
    else:
        continue