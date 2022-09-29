def anna_contri(total_item,avoided,list1,anna_provide):
    sum_total=0
    for item in range(total_item):
        if item==avoided:
            continue
        else:
            sum_total+=list1[item]
    if anna_provide-(sum_total//2)==0:
        return ("Bon Apetite")
    else:
        return anna_provide-(sum_total//2)

print(anna_contri(4,1,[3,10,2,9],7))



