def cat_and_mouse(x,y,z):
    if abs(x-z)>abs(y-z):
        print("Cat B catches the mouse")
    elif abs(x-z)<abs(y-z):
        print("Cat A catches the mouse")
    else:
        print("mosue escape")

cat_and_mouse(1,2,3)
        