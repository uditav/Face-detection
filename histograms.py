from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('photos/boston.jpeg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Grayscale histogram
# gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Grayscale masking histogram
# blank=np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('Blank',blank)
# circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# mask=cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('Mask',mask)
# gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# colour histogram
# plt.figure()
# plt.title('Colour Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# colors=('b','g','r')
# for i,col in enumerate(colors):
#     hist=cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist,color=col)
#     plt.xlim([0,256])
# plt.show()

# color masking histogram
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('Masked',masked) 
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
