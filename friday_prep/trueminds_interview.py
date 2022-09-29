dict1={'abcde' : 2, 'fgh': 3, 'ijkl': 6, 'pqrst': 4} 
dict2={'ab' :2, 'cd' : 2, 'e ' : 2, 'fgh': 3, 'ijkl ': 6, 'pqrs' : 4, 't   ' : 4}


dict2={}


def foo(dict1):
    dict1={k:v for k,v in sorted(dict1.items(),key=lambda x:x[1])}
    # print(dict1)
    for key,val in dict1.items():
        if len(key)==val:
            dict2[key]=val
        if len(key)>val:
            first=key[:val]
            dict2[first]=val
            second=key[val:]
            if len(second)>val:
                foo({second:val})
            elif len(second)<val:
                dict2[second+(val-len(second))*' ']=val
        else:
            dict2[key+((val-len(key))*' ')]=val

foo(dict1)
print(dict2)


