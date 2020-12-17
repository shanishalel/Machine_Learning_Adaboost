
class Point_for_Iris():

    #sepal =x , petal=y
    def __init__(self, point, petal_length=None, gender=None):

        if (petal_length == None):  # if its got only one param
            if isinstance(point, str):  # if its line = string from file string constructor
                arr = point.split()
                self.sepal_width = float(arr[0])
                if (arr[1] == "1"):
                    self.gender = int(arr[1])
                else:
                    self.gender = -1
                self.pulse = float(arr[2])
                self.weight = 1.0
            else:  # if its point = copy constructor
                self.temperature = point.temperature
                self.gender = point.gender
                self.pulse = point.pulse
                self.weight = 1.0

        else:  # got  temperature and pulse - and built the point
            self.temperature = point
            self.gender = gender
            self.pulse = petal_length
            # self.weight = np.longdouble(1)
            self.weight = 1.0