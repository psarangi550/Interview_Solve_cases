import os 
os.chdir("C:/Users/611903295/Downloads/interview_concept/collections_module")
path_dir=os.getcwd()
def foo(path_dir):
    size=0
    for dirnames,subdirs,files in os.walk(path_dir):
        all_subs=[sub for sub in subdirs]
        all_subs_files=all_subs+files
        for f in all_subs_files:
            mod_f=os.path.join(dirnames,f)
            if os.path.isfile(mod_f):
                file_size=os.path.getsize(mod_f)
                size+=file_size
    return size

print(foo(path_dir))
