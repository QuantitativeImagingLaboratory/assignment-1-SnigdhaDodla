import numpy as np
import cv2
import math
from resize import interpolation as inter
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here

        dim = image.shape
        reshape_x= float(fx)
        reshape_y = float(fy)
        xnew = int(reshape_x * dim[0])
        ynew = int(reshape_y * dim[1])
        Resamp_I = np.zeros((xnew, ynew), np.uint8)
        for i in range(xnew-1):
            for j in range(ynew-1):
                nx =  round(i / reshape_x)
                ny =  round(j / reshape_y)
                Resamp_I[i, j] = image[nx, ny]


        return Resamp_I


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        (ini_row, ini_col) = image.shape
        end_rfre = (float(ini_row) * float(fx))
        end_cfre = (float(ini_col) * float(fy))
        end_r = int(end_rfre)
        end_c = int(end_cfre)
        print(ini_row, ini_col, end_c, end_r)
        image1 = np.zeros((end_r, end_c), np.uint8)

        interpol = inter.interpolation()

        print("resized rows = ")
        print(end_r)
        print("resized cols = ")
        print(end_c)

        for i in range(0, end_r - 1):
            pointX1 = math.floor(i / float(fx))
            pointX2 = math.ceil(i / float(fx))
            if pointX2 == 512:
                pointX2 = 511
            for j in range(0, end_c - 1):
                pointY1 = math.floor(j / float(fy))

                pointY2 = math.ceil(j / float(fy))
                if pointY2 == 512:
                    pointY2 = 511
                # if i==0:
                #    print(pointY1,j,pointY2)

                # print(pointX1, pointY1, pointX2, pointY2)

                pt1 = (pointX1, pointY1, image[pointX1, pointY1])
                pt2 = (pointX2, pointY1, image[pointX2, pointY1])
                pt3 = (pointX1, pointY2, image[pointX1, pointY2])
                pt4 = (pointX2, pointY2, image[pointX2, pointY2])

                if isinstance(i / float(fx), float) and isinstance(j / float(fx), float):
                    unknown = (i / float(fx), j / float(fy))

                    image1[i, j] = interpol.bilinear_interpolation(pt1, pt2, pt3, pt4, unknown)
                    # bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown)
                    print(image1[i, j])

        return image1

