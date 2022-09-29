import glob
import os 
os.chdir("C:/Users/611903295/Downloads/interview_concept/collections_module")
path_dir=os.getcwd()
for file_fetch in glob.glob(f"{path_dir}/pratik.txt"):
    print(file_fetch)
