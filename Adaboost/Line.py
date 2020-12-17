from Point import Point_for_HC

class Line():
    #y=mx+n, pulse=y, temp=x
    #up=said the below is -1 and up is 1
    def __init__(self,points, up=True):
        if(up):
            self.up=True
        else:
            self.up=False
        if(points[0].temperature-points[1].temperature==0):
            self.m=(points[0].pulse-points[1].pulse)/0.000000000000000001
        else:
            self.m=(points[0].pulse-points[1].pulse)/(points[0].temperature-points[1].temperature)
        self.n=points[0].pulse-self.m*(points[0].temperature)

    #if the point is lower than the line return true
    def  is_low(self,p1):
        if self.m*p1.temperature+self.n>p1.pulse:
             return True
        else:
            return False


    #the line is right on the point
    def is_right(self,p1):
        if(self.up):
            if(self.is_low (p1)):
                return (p1.gender==-1)  ##all the -1 gender is below the line
            else:
                return (p1.gender==1)   ## all the 1 gender is above the line
        else:
            if (self.is_low(p1)):
                return (p1.gender == 1)  ##all the 1 gender is below the line
            else:
                return (p1.gender == -1)  ## all the -1 gender is above the line