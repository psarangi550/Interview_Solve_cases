class OpenFileCls(object):

    def __init__(self,filename,mode):
        print("init")
        self.filename= filename
        self.mode=mode
    
    def __enter__(self):
        print("enter the context")
        self.file=open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_value,exc_trace):
        if not self.file.closed:
            self.file.close()
        if exc_type is not None:
            print("something went wrong .....")
        print("exit")
        return True

with OpenFileCls("note.txt","w") as txt_file:
    print("do some stuff....")
    txt_file.write("to do some stuff....")
    txt_file.some()

print("continue")


