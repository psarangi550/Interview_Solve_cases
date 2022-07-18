from collections import OrderedDict
import json
input_dict = OrderedDict([('method', 'constant'), ('recursive', OrderedDict([('m', 'c')]))])
#here the dict() will not work if the order dict contains another Order dict inside it 
regular_dict=dict(input_dict)
# print(regular_dict)
#hence we need to use the json module dumps() to conver to json first and then convert to the regular dict format
json_str=json.dumps(input_dict)
# print(json_str)
#now we can convert back to the regular dict format
normal_dict=json.loads(json_str)
# print(normal_dict)

my_ord_dict=OrderedDict(normal_dict)
print(my_ord_dict)

