
from tracemalloc import Snapshot
from turtle import width
from unittest import result
import cv2
import time
import random
import dropbox

start_time = time.time()
def take_snapshot():
    number = random.randint(0,10)
    vcObject  = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vcObject.read()
        imagename = "img"+str(number)+".jpeg"
        cv2.imwrite(imagename,frame) 
        start_time = time.time
        result  = False
    return imagename 
    print("snapshot taker")
    vcObject.release()
    cv2.destroyAllWindows()
def upload_file(imagename):
    access_token = 'sl.BEE0cIbde21Qb44l1xHB4mLSKZWxwbKQjkSxqdXL6sdnGBUI3_MC8QBg1d6qwLq_JqbD8wY6ETNWjlTt_dhnyEL-qbNmbzCIQFQGWp98a1WRiEiHjP-l64PitE0lYxDtCBOL2q4A6JU'

    file_from = imagename
    file_to = "/demo/"+(imagename) # The full path to upload the file to, including the file name
    file = imagename
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if ((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)
main()
