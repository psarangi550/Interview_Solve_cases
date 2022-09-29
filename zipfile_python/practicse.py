# import zipfile #import zipfile module 
# import os #importing the os module 

# with zipfile.ZipFile("all_file.zip","w",zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write("file1.txt")
#     my_zip.write("file2.txt")
#     my_zip.write("file3.txt")
#     print("all zipping done")

# with zipfile.ZipFile("all_file.zip","r",zipfile.ZIP_STORED) as my_zip:
    # print(my_zip.namelist())
    # my_zip.extractall(os.getcwd())
    # my_zip.extract("file1.txt")

#zipping and unpacking files using shutil module 

import shutil #importing the shutil module
# shutil.make_archive("all_files","zip","my_files")
shutil.unpack_archive("all_files.zip","zip")


