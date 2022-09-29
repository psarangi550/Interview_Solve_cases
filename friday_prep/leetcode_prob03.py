from itertools import permutations 

def foo(list1):
    result=[]
    all_combo=permutations(list1,3)
    for item in all_combo:
        n_item=sorted(item)[1]
        result.append(n_item)
    if min(result)!=max(result):
        print(max(result)+min(result))
    else:
        print(min(result))

foo([2,4,1,2,7,8])   
foo([2,4,5]) 

