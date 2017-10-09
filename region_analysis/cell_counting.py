import cv2
import numpy as np
import sys
from skimage import color as sk
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        regions = dict()
        I = image
        [m, n] = I.shape
        # print(n)
        R = np.zeros((m, n), np.uint8)
        count_val = 1
        for i in range(m - 1):
            for j in range(n - 1):
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 0:
                    R[i, j] = count_val
                    count_val = count_val + 1
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 255:
                    R[i, j] = R[i - 1, j + 1]
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 0:
                    R[i, j] = R[i - 1, j]
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 0:
                    R[i, j] = R[i - 1, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 0:
                    R[i, j] = R[i, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j - 1]:
                        R[i, j] = R[i - 1, j - 1]
                    else:
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i, j - 1] = R[i - 1, j]
                        R[i, j] = R[i, j - 1]

                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j + 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i, j - 1] = R[i - 1, j + 1]
                        R[i, j] = R[i, j - 1]

                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i - 1, j - 1] == R[i - 1, j]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j] = R[i - 1, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j - 1] == R[i - 1, j + 1]:
                        R[i, j] = R[i - 1, j - 1]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j + 1]
                        R[i, j] = R[i - 1, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j] == R[i - 1, j + 1]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i, j] = R[i - 1, j]
                if I[i, j] == 255 and I[i, j - 1] == 0 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j] == R[i - 1, j + 1] == R[i - 1, j - 1]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j] = R[i - 1, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 0 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j] == R[i - 1, j + 1] == R[i, j - 1]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i, j - 1] = R[i - 1, j]
                        R[i, j] = R[i, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 0 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j + 1] == R[i - 1, j - 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j + 1]
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j] == R[i - 1, j - 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]
                if I[i, j] == 255 and I[i, j - 1] == 255 and I[i - 1, j - 1] == 255 and I[i - 1, j] == 255 and I[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j] == R[i - 1, j - 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]

        print(R)

        colored_val = sk.label2rgb(R)
        # print(colored_val.shape)

        # [k,l] = colored_val.shape
        print(count_val)

        for k in range(1, count_val):
            regions[k] = []
            for i in range(m):
                for j in range(n):
                    if R[i, j] == k:
                        regions[k].append([i, j])

        print("Regions:",regions)

        return regions


    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        final_region = dict()
        reg_count = 1
        for i in range(1, len(region) + 1):
            if (len(region[i]) > 15):
                gx = 0
                gy = 0
                for j in range(len(region[i])):
                    gx += (region[i][j][0] / len(region[i]))
                    gy += (region[i][j][1] / len(region[i]))

                final_region[reg_count] = [[int(gx), int(gy)], len(region[i])]
                reg_count += 1


        print(final_region)
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)


        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return final_region

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for i in range(1, len(stats) + 1):
            ix = stats[i][0][0]
            iy = stats[i][0][1]

            cv2.putText(image, "*", (ix, iy), cv2.QT_FONT_NORMAL, 0.2, (126, 0, 0))

        return image

