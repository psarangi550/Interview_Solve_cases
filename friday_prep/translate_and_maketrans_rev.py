str1="daabcbaabcbc"
sub_str="a"
sub_str1="a"
# table=str.maketrans({ord(sub_str):None})
# print(table)
str2=" "*len(sub_str1)
# table1=str1.maketrans(sub_str1,str2,sub_str)
# # print(table1) 
# str2=str1.translate(table1)
# print(str2)

str2=" "*len(sub_str1)
table1=str1.maketrans(sub_str1,str2)
str2=str1.translate(table1)
print(str2)