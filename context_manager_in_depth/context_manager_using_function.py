from contextlib import contextmanager #importing the context manager decorastor from contextlib module 

@contextmanager
def open_file(filename,mode):
    print("initializing the request")
    f=open(filename,mode)
    try:
        print("entering the context ")
        yield f
    finally:
        if f.closed:
            f.close()
            print("exit")

with open("xyz.txt","w") as txt_file:
    print("do something")
    txt_file.write("to do something always")