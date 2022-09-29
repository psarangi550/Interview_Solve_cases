tup1=(("a",23),("b",37),("c",11),("d",29))

tup2=()
for i in range(len(tup1)):
    for j in range(i+1,len(tup1)):
        if tup1[j][1]<tup1[i][1]:
            if tup1[j] not in tup2:
                tup2+=(tup1[j],)
            else:
                continue
        else:
            if tup1[i] not in tup2:
                tup2+=(tup1[i],)
            else:
                continue
print(tup2)