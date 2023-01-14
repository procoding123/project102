import os
import shutil

source="C:/Users/pande/Downloads"
destination="C:/Users/pande/Downloads"
files=os.listdir(source)

for file in files:
    name,ext=os.path.splitext(file)
    if ext=="":
        continue
    if ext in [".txt", ".doc", ".docx",".pdf"]:
        path1=source+"/"+file
        path2=destination+"/"+"documents"
        path3=destination+"/"+"documents"+"/"+file
        
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)

