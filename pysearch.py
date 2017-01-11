import os
curr_dir=os.getcwd()
found=0
search=input('Type file or folder to search ')
for dir,dir_names,file_names in os.walk(curr_dir):
    for d in dir_names:
        if d==search:
            found=1
            print("found matching folder in ",dir)
    for f in file_names:
        if f==search:
            found=1
            print('found matching file in',dir)
    if(found):
        break



