import cv2

im1 = cv2.imread("E:/PYTHON__/C102/1-500x250-3.jpg")
im2 = cv2.imread("E:/PYTHON__/C102/2-500x250-2.jpg")

addima = cv2.addWeighted(im1 , 0.5 , im2 , 0.5 , 0)
cv2.imwrite("E:/PYTHON__/C102/mp.png" , addima)