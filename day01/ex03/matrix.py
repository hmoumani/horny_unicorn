from Vector import Vector


class Matrix:
    def __init__(self, *argv):
        if len(argv) == 1:
            if type(argv[0]) == list:
                if any([len(argv[0][0]) != len(argv[0][i]) for i in range(1, len(argv[0]))]):
                    print("ERROR")
                    exit(1)
                self.data = argv[0].copy()
                self.shape = (len(argv[0]), len(argv[0][0]))
            elif type(argv[0]) == tuple:
                if len(argv[0]) != 2:
                    print("ERROR")
                    exit(1)
                self.shape = argv[0]
                self.data = [[0 for i in range(self.shape[0])] for i in range(self.shape[1])]
            else:
                print("unsupported format")
        elif len(argv) == 2:
            if type(argv[0]) != list or type(argv[1]) != tuple:
                print("unsupported format")
                exit(1)
            else:
                if len(argv[1]) != 2 or len(argv[0]) != argv[1][0] or any([len(elem) != argv[1][1] for elem in argv[0]]):
                    print("ERROR")
                    exit(1)
                
    def __add__(self, x):
        if self.size != x.size:
            return print("matrices should be in the same size")
        if type(x) == Matrix:
            return Matrix([[self.data[i][j] + x.data[i][j] for j in self.shape[1]] for i in self.shape[0]])
        else:
            return print("undefined")

    __radd__ = __add__

    def __sub__(self, x):
        if self.size != x.size:
            return print("matrices should be in the same size")
        if type(x) == Matrix:
            return Matrix([[self.data[i][j] - x.data[i][j] for j in self.shape[1]] for i in self.shape[0]])
        else:
            return print("undefined")

    def __rsub__(self, x):
        if self.size != x.size:
            return print("matrices should be in the same size")
        if type(x) == Matrix:
            return Matrix([[x.data[i][j] - self.data[i][j] for j in self.shape[1]] for i in self.shape[0]])
        else:
            return print("undefined")

    def __truediv__(self, x):
        if type(x) == int:
            if x == 0:
                return print("undefined")
            return Matrix([[num / x for num in elem] for elem in self.data])
        else:
            return print("undefined")
    def __rtruediv__(self, x):
        if type(x) == int:
            return Matrix([[x / num for num in elem] for elem in self.data])
        else:
            return print("undefined")
    def __mul__(self, x):
        if type(x) == int:
            return Matrix([[num * x for num in elem] for elem in self.data])
        elif type(x) == Matrix:
            if self.shape[1] != x.shape[0]:
                return print("undefined")
            else:
                return Matrix([[sum([self.data[i][k] * x.data[k][j] for k in range(self.shape[1])]) for j in range(x.shape[1])] for i in range(self.shape[0])])
        if type(x) == Vector:
            if x.size != self.shape[1]:
                return print("undefined")
            return Vector([sum([self.data[i][j] * x.values[j] for j in range(self.shape[1])]) for i in range(self.shape[0])]) 
        else:
            return print("undefined")
    def __rmul__(self, x):
        return self * x
    def __str__(self):
        return "data: {}, shape: {}".format(self.data, self.shape)
    def __repr(self):
        return "Matrix(data={}, shape={})".format(self.data, self.shape)