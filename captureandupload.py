import cv2
import random
import time
import dropbox

start_time=time.time()
def snap():
    number=random.randint(0 , 100)
    vcObj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret , frame=vcObj.read()
        imgName="img" + str(number) + ".png"
        cv2.imwrite(imgName , frame)
        start_time= time.time
        result=False
    return(imgName)    
    print("Snapshot Taken")
    vcObj.release()
    cv2.destroyAllWindows()

def uploadFiletoDropbox( imgName ):
        accessToken="sl.BJE7PwFd4WjUBXCvEjTB_EzHZ3X5OUmtS5BjG0du24IN2_eaIYakgoFIW4QJlMJEqeLszoCHq4RTAQ4Lx7Mi1WJa-edr2WMvQt2jpCKIZSYzCb3TqUqnOpXE1AFiIKd0WjsMgEsTXiY"
        file=imgName
        fileFrom=file
        fileTo="/userPictures/" + "(imgName)"
        dbx=dropbox.Dropbox(accessToken)
        with open(fileFrom , 'rb') as f:
          # to resolve the path errors last parameter is added
            dbx.files_upload(f.read(), fileTo , mode=dropbox.files.WriteMode.overwrite )
            print("File Sucsessfully Uploaded")
def main():
    while(True):
        if((time.time() - start_time )>=5 ):
            name=snap()
            uploadFiletoDropbox(name)

main()