def foo(total_page,page):
    if (total_page-page)>page:
        print(" from front side",((page)//2))
    else:
        if total_page%2==0 and page%2!=0:
            print("from back sides",(((total_page-page)+1)//2))
        else:
            print("from back sides",((total_page-page)//2))

# foo(7,3)
foo(6,5)
