# import rtsp

# #RTSP_URL = f"rtsp://{USERNAME}:{PASSWORD}@172.21.72.122/22"

# with rtsp.Client(rtsp_server_uri = 'rtsp://admin:pass@172.21.72.122:8554/cam') as client:
# 	client.preview()
# #192.169.0.37 
# #192.168.0.255

import cv2
cap_txa = cv2.VideoCapture("rtsp://172.21.72.122:8554/cam")
#cap_adem = cv2.VideoCapture("rtsp://192.169.0.37:8554/cam")

cap = cap_txa

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()