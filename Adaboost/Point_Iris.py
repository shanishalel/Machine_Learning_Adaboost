
class Point_for_Iris():

    #sepal =x , petal=y
    def __init__(self, point, petal_length=None, gender=None):

        if (petal_length == None):  # if its got only one param
            if isinstance(point, str):  # if its line = string from file string constructor
                arr = point.split(",")
                self.sepal_width = float(arr[1])
                if (arr[4] == "Iris-versicolor\n"):
                    self.gender = 1
                else :  #Iris-virginica
                    self.gender = -1
                self.petal_length = float(arr[2])
                self.weight = 1.0
            else:  # if its point = copy constructor
                self.sepal_width = point.sepal_width
                self.gender = point.gender
                self.petal_length = point.petal_length
                self.weight = 1.0

        else:  # got  temperature and pulse - and built the point
            self.sepal_width = point
            self.gender = gender
            self.petal_length = petal_length
            # self.weight = np.longdouble(1)
            self.weight = 1.0