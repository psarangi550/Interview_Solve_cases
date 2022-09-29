def social_media(share_number,days):
    count=0
    total=0
    for i in range(1,days+1):
        count=share_number//2 #2 #3 #4 #6 #9
        total+=count
        share_number=count*3 #6 #9 #12 #18 #27
    return total

print(social_media(5,5))
