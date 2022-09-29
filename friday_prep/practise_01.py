str1="156469494949"
# output={"1":"5","5":6,"6":"4","4":6}
list1=[]
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if i%2 == 0:
            tup1=(str1[i],str1[j])
        else:
            tup1=(str1[i],int(str1[j]))
        list1.append(tup1)
        break
print(list1)   

