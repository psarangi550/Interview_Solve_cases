import re #importing the re module 

list1=[
    "https://www.google.com",
    "http://coreyms.com",
    "https://youtube.com",
    "https://www.youtube.com",
]

pattern="^(http|https)://(www\.)?\w+\.\w+"

pt=re.compile(pattern=pattern)

for item in list1:
    iter_match=pt.finditer(item)
    for match in iter_match:
        print(match.group())
