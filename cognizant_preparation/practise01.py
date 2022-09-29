list1=[50,60,60,45,70]
sum_team1=sum_team2=0
result=[]
for ele in range(len(list1)):
    if ele%2==0:
        sum_team1+=list1[ele]
    else:
        sum_team2+=list1[ele]
result.extend((sum_team1,sum_team2))
print(result)


