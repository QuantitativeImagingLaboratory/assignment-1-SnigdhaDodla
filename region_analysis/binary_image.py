
import cv2
import numpy as np
import sys
import os
from random import uniform
import matplotlib.pyplot as plt


class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        (row, col) = image.shape
        hist = [0] * 256

        for i in range(row):
            for j in range(col):
                hist[image[i, j]] += 1

        return hist

    def find_optimal_threshold(self,thresh,hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        count =0;
        intensity = list()

        for i in range(0, 256):
            if (hist[i] != 0):
                intensity.append(i)



        k = intensity[0]
        j = intensity[-1]

        min_intensity = min(intensity)
        max_intensity = max(intensity)

        sum_t = 0
        count_t = 0
        sum_end = 0
        count_end = 0
        t = 0
        thresh_data = round(thresh)
        for x in range(0, thresh_data):
            sum_t = sum_t + intensity[x]
            count_t = count_t + 1

        mean_thresh = sum_t / count_t
        for y in range(thresh_data, len(intensity)):
            sum_end = sum_end + intensity[y]
            count_end = count_end + 1

        mean_end = sum_end / count_end
        avg = round((mean_thresh + mean_end) / 2)
        while 1:
            if (abs(avg - thresh_data) == 0):
                thresh_data = avg
                t = 1
                # print(thresh_data)
                break
            else:
                t = 0
                c = self.find_optimal_threshold(avg,hist)

                thresh_data = c
                break

            if t == 1:
                thresh_data = avg
                print(thresh_data)
                break

        return thresh_data



    def binarize(self, image,a):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        [k, l] = image.shape
        I_binary = image
        #print(image)
        print("assigned", I_binary)
        for i in range(0, k):
            for j in range(0, l):
                if (image[i, j]) < a:
                    I_binary[i, j] = 255
                else:
                    I_binary[i, j] = 0

        print("evauated", I_binary)
        I_binary = image.copy()
        print(I_binary)
        return I_binary
        bin_img = image.copy()




