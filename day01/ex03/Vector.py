class Vector:
    def __init__(self, param):
        if type(param) == list:
            self.values = param
            self.size = len(param)
        elif type(param) == int:
            self.values = [float(elem) for elem in list(range(param))]
            self.size = len(self.values)
        elif type(param) == tuple:
            self.values = [float(elem) for elem in list(range(param[0], param[1]))]
            self.size = len(self.values)
    def __add__(self, x):
        if type(x) == int:
            return Vector([elem + x for elem in self.values])
        if type(x) == Vector:
            if x.size != self.size:
                print("Vectors should be in the same size")
                return None
            return Vector([self.values[i] + x.values[i] for i in range(self.size)])
        return print("undefined")
        
    __radd__ = __add__
    def __sub__(self, x):
        if type(x) == int:
            return Vector([elem - x for elem in self.values])
        if type(x) == Vector:
            if x.size != self.size:
                print("Vectors should be in the same size")
                return None
            return Vector([self.values[i] - x.values[i] for i in range(self.size)])
        return print("undefined")
        
    def __rsub__(self, x):
        if type(x) == int:
            return Vector([x - elem for elem in self.values])
        if type(x) == Vector:
            if x.size != self.size:
                print("Vectors should be in the same size")
                return None
            return Vector([x.values[i] - self.values[i] for i in range(self.size)])
        return print("undefined")
        
    def __truediv__(self, x):
        if type(x) == int:
            return Vector([elem / x for elem in self.values])
        elif type(x) == Vector:
            print("cannot devide two Vectors")
            return None
        return print("undefined")
        

    def __rtruediv__(self, x):
        if type(x) == int:
            return Vector([x  / elem for elem in self.values])
        elif type(x) == Vector:
            print("cannot devide two Vectors")
            return None
        return print("undefined")
        
    def __mul__(self, x):
        if type(x) == int:
            return Vector([elem * x for elem in self.values])
        elif type(x) == Vector:
            if (x.size != self.size):
                print("Vectors should be in the same size")
                return None
            return sum([x.values[i] * self.values[i] for i in range(self.size)])
        return NotImplemented
    
    def __rmul__(self, x):
        if type(x) == int:
            return Vector([elem * x for elem in self.values])
        return print("undefined")
    def __str__(self):
        return "elements : {}, size : {}".format(self.values, self.size)

    def __repr__(self):
        return "Vector(values={}, size={})".format(self.values, self.size)