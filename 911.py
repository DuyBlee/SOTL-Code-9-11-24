import cv2
import numpy
cam = cv2.VideoCapture(0)

def grayscale(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

def chimtohayho(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 9, 250, 250)
    cthh = cv2.bitwise_and(color, color, mask=edges)
    return cthh

filter = "normal"   
while True:
    check, frame = cam.read()
    
    if filter == "grayscale":
        frame = grayscale(frame)
    if filter == "chimtohayho":
        frame = chimtohayho(frame)

    cv2.imshow("video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('e'):
        filter = 'grayscale'
    elif key == ord('r'):
        filter = 'chimtohayho'        
    elif key == ord('t'):
        filter = 'normal'   

cam.release()
cv2.destroyAllWindows()