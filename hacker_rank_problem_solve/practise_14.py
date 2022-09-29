def pair_of_sock(total,list1):
    result = []
    dict1={}
    for i in range(len(list1)):
        count=1
        for j in range(i+1,len(list1)):
            if list1[i]== list1[j]:
                count+=1
        result.append({list1[i]:count})
    # return result
    for ele in result:
        if tuple(ele.keys()) not in dict1:
            dict1[(tuple(ele.keys()))] =tuple(ele.values())[0]
        else:
            pass
    return dict1

    

print(pair_of_sock(9,[10,20,20,10,10,30,50,10,20]))
