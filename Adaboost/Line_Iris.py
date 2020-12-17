from Point_Iris import Point_for_Iris

class Line_Iris():
    # sepal =x , petal=y
    def __init__(self, points,up=True):
        if(up):
            self.up=True
        else:
            self.up=False
        if (points[0].sepal_width - points[1].sepal_width == 0):
            self.m = (points[0].petal_length - points[1].petal_length) / 0.000000000000000001
        else:
            self.m = (points[0].petal_length - points[1].petal_length) / (points[0].sepal_width - points[1].sepal_width)
        self.n = points[0].petal_length - self.m * (points[0].sepal_width)

    # if the point is lower than the line return true
    def is_low(self, p1):
        if self.m * p1.sepal_width + self.n > p1.petal_length:
            return True
        else:
            return False

    # the line is right on the point
    def is_right(self, p1):
        if(self.up):
            if (self.is_low(p1)):
                return (p1.gender == -1)  ##all the -1 gender is below the line
            else:
                return (p1.gender == 1)  ## all the 1 gender is above the line
        else:
            if (self.is_low(p1)):
                return (p1.gender == 1)  ##all the 1 gender is below the line
            else:
                return (p1.gender == -1)  ## all the -1 gender is above the line





