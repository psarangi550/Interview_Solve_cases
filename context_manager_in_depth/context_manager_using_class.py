class OpenFile(object):
    
    def __init__(self, filename,mode):
        print("executing the init function")
        self.filename = filename
        self.mode=mode
        
    def __enter__(self):
        print("entering the context manager")
        self.file=open(self.filename,self.mode)
        return self.file #returning the file object
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file.closed:
            self.file.close()
        print("exit")

with OpenFile("abc.txt","w") as txt_file:
    print("do some stuff ....")
    txt_file.write("To do something")