from tkinter import Frame
import cv2

vP = cv2.VideoCapture(0)
ret , frame = vP.read()
cv2.imwrite("E:/PYTHON__/C102/mp.png" , frame)
vP.release()
cv2.destroyAllWindows()
