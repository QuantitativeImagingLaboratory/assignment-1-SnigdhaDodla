class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        newIntensity = 0
        x = 0
        y = 0
        point1, itensity1 = pt1
        point2, intensity2 = pt2
        newPoint = unknown
        changeIntensity = point2 - point1
        if (changeIntensity == 0):
            changeIntensity = 1

        a1 = point2 - newPoint
        b1 = a1 / changeIntensity
        x = itensity1 * b1
        a2 = newPoint - point1
        b2 = a2 / changeIntensity
        y = intensity2 * b2

        newIntensity = x + y
        if (newIntensity > 255):
            newIntensity = newIntensity - 255

        return newIntensity



    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        pointX1, pointY1, intensity1 = pt1
        pointX2, pointY2, intensity2 = pt2
        pointX3, pointY3, intensity3 = pt3
        pointX4, pointY4, intensity4 = pt4
        newPointX1, newPointY1 = unknown

        newInt1 = self.linear_interpolation((pointX1, intensity1), (pointX2, intensity2), newPointX1)
        newInt2 = self.linear_interpolation((pointX3, intensity3), (pointX4, intensity4), newPointX1)
        newpt1 = pointY1, newInt1
        newpt2 = pointY4, newInt2
        finalIntensity = self.linear_interpolation(newpt1, newpt2, newPointY1)
        return finalIntensity

