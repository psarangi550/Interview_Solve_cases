import os 
os.chdir("C:/Users/611903295/Downloads/interview_concept/collections_module")
path_dir=os.getcwd()
def foo(path_dir):
    # count=0
    for dirname,subdirs, files in os.walk(path_dir):
        all_subs=[sub for sub in subdirs]
        all_subs_files=all_subs+files
        for f in all_subs_files:
            mode_f=os.path.join(dirname,f)
            if os.path.isfile(mode_f) and not f.endswith(".py") and f=="newsub1.txt":
                print("{0:<65}{1} ".format("file size is ",os.path.getsize(mode_f)))
                print(dirname)
            # print()
    # print(count)

foo(path_dir)