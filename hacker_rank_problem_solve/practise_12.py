def migrate_birds(arr):
    total=[0]*len(arr)
    for ele in arr:
        total[ele]+=1
    # print(total)
    return total.index(max(total))

print(migrate_birds([1,1,2,2,3]))

