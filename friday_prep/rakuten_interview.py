# def after_n_days([Thursday,Monday], 4):
#      [Monday,Friday]

from itertools import cycle
list1=["Mon","Tue","Wed","Thr","Fri","sat","sun"]
def after_n_days(list2,num):
    result=[]
    for ele in list2:
        val=bar(ele,num)
        result.append(val)
    return result

def bar(list2,num):
    count=0
    cycle_list=cycle(list1)
    for item in cycle_list:
        if item==list2:
            for item in cycle_list:
                count+=1
                if count==num:
                    return item
                    break
            break
    

    
print(after_n_days(["Mon","Thr"],4))