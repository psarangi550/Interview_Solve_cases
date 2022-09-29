import os 
os.chdir("C:/Users/611903295/Downloads/interview_concept/collections_module")
path_dir=os.getcwd()
def foo(path_dir):
    for dirnames,subs,files in  os.walk(path_dir):
        print(dirnames)
        all_sub=[sub for sub in subs]
        # print(all_sub)
        all_sub_file=all_sub+files
        # print(all_sub_file)
        for f in all_sub_file:
            mod_f=os.path.join(dirnames,f)
            if os.path.isfile(mod_f):
                print("just the file",f)
        print()

def bar(path_dir):
    for dirnames,subdirs,files in os.walk(path_dir):
        print(dirnames)
        all_sub=[sub for sub in subdirs]
        for f in all_sub:
            mod_f=os.path.join(dirnames,f)
            if os.path.isdir(mod_f):
                print("just the subdir",f)


# foo(path_dir)
bar(path_dir)