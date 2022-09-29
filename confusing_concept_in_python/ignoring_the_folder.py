import os 
os.chdir("C:/Users/611903295/Downloads/interview_concept/collections_module")
path_dir=os.getcwd()
def foo(path_dir):
    count_dir=0
    for dirnames,subdirs,files in os.walk(path_dir):
        all_sub=[sub for sub in subdirs if not sub.endswith("sub1")]
        print(all_sub)
        for f in all_sub:
            mod_f=os.path.join(dirnames,f)
            if os.path.isdir(mod_f):
                count_dir+=1
                print("just the subdir",f)
    print(count_dir)

foo(path_dir)


