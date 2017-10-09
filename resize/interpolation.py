class interpolation:
    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for linear interpolation here

        new_i = 0
        x = 0
        y = 0
        p1, i1 = pt1
        p2, i2 = pt2
        newPoint = unknown
        new_i = p2 - p1
        if (new_i == 0):
            new_i = 1

        a1 = p2 - newPoint
        b1 = a1 / new_i
        x = i1 * b1
        a2 = newPoint - p1
        b2 = a2 / new_i
        y = i2 * b2

        new_i = x + y
        if (new_i > 255):
            new_i = new_i - 255

        return new_i

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear intaerpolation for the unknown values using pt1 and pt2
               take as input
               pt1: known point pt1 and f(pt1) or intensity value
               pt2: known point pt2 and f(pt2) or intensity value
               pt1: known point pt3 and f(pt3) or intensity value
               pt2: known point pt4 and f(pt4) or intensity value
               unknown: take and unknown location
               return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        px1, pointY1, i1 = pt1
        px2, pointY2, i2 = pt2
        px3, pointY3, i3 = pt3
        px4, pointY4, i4 = pt4
        newpx1, newPointY1 = unknown

        newInt1 = self.linear_interpolation((px1, i1), (px2, i2), newpx1)
        newInt2 = self.linear_interpolation((px3, i3), (px4, i4), newpx1)
        newpt1 = pointY1, newInt1
        newpt2 = pointY4, newInt2
        final_i = self.linear_interpolation(newpt1, newpt2, newPointY1)
        return final_i




