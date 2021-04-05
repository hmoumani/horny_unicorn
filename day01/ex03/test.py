from matrix import Matrix
from Vector import Vector

# m0 = Matrix((2, 3))

# m1 = Matrix([[1,3,4],[5,6,7]])

# m2 = Matrix([[1,3,4],[5,6,7]], (2, 3))

# A=Matrix([[1,4,-2],[3,5,-6]])

# B=Matrix([[5,2,8,-1], [3,6,4,5], [-2,9,7,-3]])

# C = A * B

# print(C.data)


A=Matrix([[1, -1,2], [0, -3, 1]])
B=Vector([2,1,0])

C = B*A

print(C.values)