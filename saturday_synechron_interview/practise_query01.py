# Given a two dimensional list, for example [ [2,3],[3,4],[5]] 
# person 2 is friends with 3 etc, 
# find how many friends each person has. Note, one person has no friends.
# {2: 1, 3: 2, 4: 1, 5: 0}

list1=[[2,3],[3,4],[5]] 

dict1={}

for ele in list1:
    c=len(ele)
    for index in ele:
        if index not in dict1 and c==2:
            dict1[index]=1
        elif index not in dict1 and c==1:
            dict1[index]=0
        else:
            dict1[index]+=1

print(dict1)