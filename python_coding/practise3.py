#pascal triangle



def foo():
    result=[[] for i in range(5)]
    for i in range(5):
        for j in range(i+1):
            if j < i:
                if j==0:
                    result[i].append(1)
                else:
                    num=(result[i-1][j-1]+result[i-1][j])
                    result[i].append(num)
            elif i==j:
                    result[i].append(1)
    

    return result

print(foo())
# print(result)
