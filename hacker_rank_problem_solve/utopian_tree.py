from itertools import cycle
season_list=["summer","spring"]
def utopian_tree(num):
    tree_cycles=cycle(season_list)
    height=0
    result=[]
    for i in range(num+1):
        for tree_cycle in tree_cycles:
            if tree_cycle=="summer" and i%2==0:
                height+=1
                result.append(height)
                break
            elif tree_cycle=="spring" and i%2!=0:
                height*=2
                result.append(height)
                break
    print(max(result))  
# utopian_tree(5)
# utopian_tree(6)
utopian_tree(0)
utopian_tree(1)
utopian_tree(4)