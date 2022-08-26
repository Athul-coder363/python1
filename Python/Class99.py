import os 
import shutil
#os.system('date')

#os.mkdir("newfolder1")
"""
print(os.getcwd)
path = 'C:/Users/Incre/Python'
isExist = os.path.exists(path)
print(isExist)

path1 = 'C:/Users/Incre/Python/text.txt'
root_ext=os.path.splitext(path1)
print("root part:",root_ext[0])
print("extension path:", root_ext[1])

print(os.listdir())
"""


source = input("Please enter the source:")
destination = input("Please enter the destination:")
source = source+'/'
destination = destination+'/'
listOfDir = os.listdir(source)
for file in listOfDir:
    shutil.copy((source+file),destination)

