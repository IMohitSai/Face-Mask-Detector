import cv2
import uuid
import os


cap = cv2.VideoCapture(0)

save_path = './Images/Nomask/'
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()  

    if not ret:
        print("Failed to capture image")
        break  

    
    imgname = './Images/Nomask/{}.jpg'.format(str(uuid.uuid1()))
    cv2.imwrite(imgname, frame)

    
    cv2.imshow('frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  


cap.release()
cv2.destroyAllWindows()
