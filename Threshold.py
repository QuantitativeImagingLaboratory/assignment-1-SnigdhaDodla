import cv2
import numpy as np
import sys
import random
import matplotlib.pyplot as plt
def histo(image):
    (row, col) = image.shape
    hist = [0] * 256

    for i in range(row):
        for j in range(col):
            hist[image[i, j]] += 1

    return hist

cells = cv2.imread("cells.png", 0)
image_hist1 = histo(cells)
plt.plot(image_hist1)
plt.show()
intensity = list(range(1,256))
frequency = list(range(1,256))
k= intensity[0]
j=intensity[-1]
#print(j)

#intense = np.array(intensity)

#k = intense.shape[1]
#print(k)
sum_t =0
count_t=0
sum_end=0
count_end=0
min_intensity = min(intensity)
max_intensity = max(intensity)
rand_val= min_intensity+(max_intensity-min_intensity)*random.uniform(0,1)

def find_avg(thresh,sum_t,count_t,sum_end,count_end):
    t=0
    thresh_data = round(thresh)
    for x  in range(k,thresh_data):
        sum_t = sum_t +intensity[x]
        count_t = count_t +1
        print(count_t)

    mean_thresh = sum_t/count_t
    for y in range(thresh_data,j):
        sum_end = sum_end+intensity[y]
        count_end = count_end +1
        print(count_end)

    mean_end = sum_end/count_end
    avg = round((mean_thresh+mean_end)/2)
    print(avg)
    while 1:
        if(abs(avg-thresh_data)<=5):
            thresh_data = avg
            t = 1
        else :
            t=0
            find_avg(avg,0,0,0,0)
        if t==1:
            thresh_data = avg
            break



a = find_avg(rand_val,sum_t,count_t,sum_end,count_end)
print(a)




