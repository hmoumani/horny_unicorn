class Vector:
    def __init__(self, param):
        if isinstance(param, list):
            if not all(isinstance(elem, list) for elem in param):
                raise TypeError("param should be a list of list of floats")
            if not all(isinstance(number, float) for elem in param
                       for number in elem):
                raise TypeError("param should be a list of list of floats")
            if not all(len(elem) == 1 for elem in param) and len(param) != 1:
                raise ValueError("A vector is either a single line of floats\
                    or a single column of floats.")
            self.values = param
            self.shape = (len(param), len(param[0]) if param else 0)
        elif isinstance(param, int):
            if param < 0:
                raise ValueError("param should be a positive integer")
            if param == 0:
                self.values = []
                self.shape = (0, 0)
                return
            self.values = [[float(i)] for i in range(param)]
            self.shape = (param, 1)
        elif isinstance(param, tuple):
            if not len(param) == 2\
                    or not all(isinstance(elem, int) for elem in param):
                raise TypeError("param should be a tuple of two integers")
            if param[0] > param[1]:
                raise ValueError(
                    "The first element of the tuple should be smaller\
                        than the second one")
            self.values = [[float(i)] for i in range(param[0], param[1])]
            self.shape = (param[1] - param[0], 1)
        else:
            raise TypeError(
                "param should be a list of list of floats, an integer or\
                    a tuple of two integers")

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("other should be a Vector")
        if self.shape != other.shape:
            raise ValueError("Vectors should be in the same shape")
        return sum(self.values[i][j] * other.values[i][j]
                   for i in range(self.shape[0]) for j in range(self.shape[1]))

    def T(self):
        return Vector([[self.values[j][i] for j in range(self.shape[0])]
                       for i in range(self.shape[1])])

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("other should be a Vector")
        if self.shape != other.shape:
            raise ValueError("Vectors should be in the same shape")
        return Vector([[self.values[i][j] + other.values[i][j]
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("other should be a Vector")
        if self.shape != other.shape:
            raise ValueError("Vectors should be in the same shape")
        return Vector([[self.values[i][j] - other.values[i][j]
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("other should be a number")
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Vector([[self.values[i][j] / other
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("other should be a number")
        raise ArithmeticError(
            "Division of a scalar by a Vector is not defined here.")

    def __mul__(self, other):
        if isinstance(other, Vector):
            NotImplementedError(
                "Multiplication of two vectors is not defined here.")
        if not isinstance(other, (int, float)):
            raise TypeError("other should be a number")
        return Vector([[self.values[i][j] * other
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self) -> str:
        return str(self.values)

    def __repr__(self) -> str:
        return str(self.values)
