from string import ascii_lowercase
import random
heights=[random.randint(1,7) for _ in range(27)]
def pdf_area(heights,str1):
    char_height=dict(zip(ascii_lowercase,heights))
    print(char_height)
    max_height=0
    for ele in str1:
        if char_height[ele]>=max_height:
            max_height = char_height[ele]
    return max_height*len(str1)

print(pdf_area(heights,"ab"))

