def money_for_keyboard(keys,usbs,total):
    max_val=[]
    for key in keys:
        for usb in usbs:
            if key+usb>total:
                continue
            else:
                max_val.append(key+usb)
    if len(max_val)==0:
        return -1
    else:
        return max(max_val)

# print(money_for_keyboard([3,1],[5,2,8],10))
# print(money_for_keyboard([40,50,60],[5,8,12],60))
print(money_for_keyboard([4],[5],5))