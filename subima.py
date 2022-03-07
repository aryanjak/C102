import cv2

im1 = cv2.imread("E:/PYTHON__/C102/star-1-300x168.jpg")
im2 = cv2.imread("E:/PYTHON__/C102/dot-300x168.jpg")

subima = cv2.subtract(im1 , im2)
cv2.imwrite("E:/PYTHON__/C102/sp.png" , subima)