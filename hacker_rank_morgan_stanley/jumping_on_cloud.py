def energy(c,k):
    unit=100
    index=None
    for i in range(0,len(c),k):
        index=(i+k)%len(c)
        print(c[index])
        if c[index]==1:
            unit=unit-3
        elif c[index]==0:
            unit=unit-1
        elif index==0:
            unit=unit-1
            break

    return unit

print(energy([0,0,1,0,0,1,1,0],2))



