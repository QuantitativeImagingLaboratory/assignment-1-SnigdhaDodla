import cv2
import numpy as np
import sys
import os
from random import uniform
import matplotlib.pyplot as plt

def histo(image):
    (row, col) = image.shape
    hist = [0] * 256

    for i in range(row):
        for j in range(col):
            hist[image[i, j]] += 1

    return hist

#cells = cv2.imread("cells.png", 0)
#image_hist1 = histo(cells)
#plt.plot(image_hist1)
#plt.show()
intensity = list(range(0,256))
frequency = list(range(0,256))
k= intensity[0]
j=intensity[-1]
#print(j)

#intense = np.array(intensity)

#k = intense.shape[1]
#print(k)


min_intensity = min(intensity)
max_intensity = max(intensity)
rand_val= min_intensity+(max_intensity-min_intensity)*uniform(0,1)
print(rand_val)


def find_avg(thresh):
    sum_t =0
    count_t=0
    sum_end=0
    count_end=0
    t=0
    thresh_data = round(thresh)
    for x  in range(k,thresh_data):

        sum_t = sum_t +intensity[x]
        count_t = count_t +1


    mean_thresh = sum_t/count_t
    for y in range(thresh_data,j):
        sum_end = sum_end+intensity[y]
        count_end = count_end +1


    mean_end = sum_end/count_end
    avg = round((mean_thresh+mean_end)/2)
    while 1:
        if(abs(avg-thresh_data)==0):
            thresh_data = avg
            t = 1
            #print(thresh_data)
            break
        else :
            t = 0
            c= find_avg(avg)
            print("c value is",c)
            thresh_data = c
            break

        if t ==1:
           thresh_data = avg
           print(thresh_data)
           break


    return thresh_data

def binarize(image,a):
    [k,l] = image.shape
    I_binary = image
    print(image)
    print("assigned",I_binary)
    for i in range(0,k):
        for j in range(0,l):
            if(image[i,j])< a:
                I_binary[i,j] = 255
            else:
                I_binary[i,j] = 0

    print("evauated",I_binary)
    return I_binary
cells = cv2.imread("cells.png", 0)
print(cells)
image_hist1 = histo(cells)
a = find_avg(rand_val)
print("threshold",cells)
print("avg is",a)
b=76
Image_bin = binarize(cells,a)
#print(Image_bin)
#print("Original",cells)
cv2.imshow("Binary",Image_bin)
cv2.waitKey(10000000)











