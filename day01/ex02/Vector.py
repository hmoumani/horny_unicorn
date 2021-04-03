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
            for elem in self.values:
                elem += x

print(Vector((10,16)).values)