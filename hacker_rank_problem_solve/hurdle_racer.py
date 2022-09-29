def hurdle_race(hurdles,height):
    max_height=hurdles[0]
    for hurdle in hurdles:
        if hurdle>max_height:
            max_height=hurdle
    if max_height>height:
        print("portion rerquired is",max_height-height)
    else:
        print("portion required is",0)

hurdle_race([2,5,4,5,2],7)
hurdle_race([1,2,3,3,2],1)