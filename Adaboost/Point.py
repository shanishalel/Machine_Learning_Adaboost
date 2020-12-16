
#point class to HC
class Point_for_HC():

    ##(1,1,3)>
    def __init__(self, point, pulse=None, gender=None):

        if (pulse == None):  # if its got only one param
            if isinstance(point, str):  # if its line = string from file string constructor
                arr = point.split()
                self.temperature = float(arr[0])
                if (arr[1] == "1"):
                    self.gender = int(arr[1])
                else:
                    self.gender = -1
                self.pulse = float(arr[2])
                self.weight = 1.0/130
            else:  # if its point = copy constructor
                self.temperature = point.temperature
                self.gender = point.gender
                self.pulse = point.pulse
                self.weight = 1.0/130

        else:  # got  temperature and pulse - and built the point
            self.temperature = point
            self.gender = gender
            self.pulse = pulse
            # self.weight = np.longdouble(1)
            self.weight = 1.0/130



