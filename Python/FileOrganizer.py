import os
import shutil

path = input("Please enter the path of your directory:")
listFiles = os.listdir(path)
print(listFiles)

for i in listFiles:
    name,est = os.path.splitext(i)
    est = est[1:]
    if est == '':
        continue
    if os.path.exists(path+'/'+est):
        shutil.move(path+'/'+i,path+'/'+est+'/'+i)
    else:
        os.mkdir(path+'/'+est)
        shutil.move(path+'/'+i,path+'/'+est+'/'+i)