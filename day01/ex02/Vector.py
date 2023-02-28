class Vector:
    def __init__(self, param):
        if not isinstance(param, list) or not all(isinstance(elem, list) for elem in param)\
            or not all(isinstance(number, float) for elem in param for number in elem):
            raise TypeError("param should be a list of list of floats")
        if not all(len(elem) == 1 for elem in param) and len(param) != 1:
            raise ValueError("A vector is either a single line of floats or a single column of floats.")
        self.values = param
        self.shape = (len(param), len(param[0]) if param else 0)

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("other should be a Vector")
        if self.shape != other.shape:
            raise ValueError("Vectors should be in the same shape")
        return sum(self.values[i][j] * other.values[i][j] for i in range(self.shape[0]) for j in range(self.shape[1]))
    
    def T(self):
        return Vector([[self.values[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])])
   
   
if __name__ == "__main__":
    v1 = Vector([[-5., -7.]])
    print(v1.T().values)
    v2 = Vector([[0., 7.]])
    print(v2.T().values)


    # print(v1.dot(v2))

    v3 = Vector([[1.0, 3.0]])
    print(v3.T().values)

    v4 = Vector([[2.0], [4.0]])
    print(v4.T().values)

    v4 = Vector([])
    print(v4.T().values)

    # print(v3.dot(v4))

    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    # print(v1.dot(v2))