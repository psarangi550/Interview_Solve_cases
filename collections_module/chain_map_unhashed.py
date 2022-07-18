from collections import ChainMap

dict1={"roll":101,"name":"rika"}
dict2={"addr":"bangalore"}
#unpacking the dict and merging at the same time 
dict3={**dict1,**dict2}
print(dict3)
#or here we can use the update () of the dictionary as 
dict4={}#creating a empty dict object
dict4.update(dict3)
print(dict4)
#here doing the chain mapping the dict object 
chain_dict=ChainMap(dict1,dict2)
print(chain_dict)
