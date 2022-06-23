import cv2
catcher = cv2.VideoCapture(0)
while (true):
    index, frame = catcher.read()
    cv2.imshow('CAPTURANDO VIDEO', frame)
    
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BAYER_GB2GRAY)
    cv2.imshow('CAPTURANDO EN GRISES', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    cv2.release()
    
    cv2.destroyAllWindows()