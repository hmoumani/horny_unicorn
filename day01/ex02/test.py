from vector import Vector

# initialize a vector tests #

# using a list of lists and a list of floats

v = Vector([[float(i)] for i in range(10)])

v1 = Vector([[float(i) for i in range(10)]])

# v2 = Vector([[1., 2., 3., 4., 'q']]) # should raise an error

# v3 = Vector([[1., 2., 3., 4., 5.], [1., 2., 3., 4., 5.]]) # raise an error

# using a tuple for range

v4 = Vector((0, 10))

v5 = Vector((10, 20))

# v4 = Vector((20, 10)) # should raise an error

# v5 = Vector((0, 10, 20)) # should raise an error

# using an integer

v6 = Vector(10)

v7 = Vector(20)

v8 = Vector(1)

# v9 = Vector(-10) # should raise an error

# math operations #

# dot product

v1 = Vector([[float(i)] for i in range(10)])
v2 = Vector([[float(i * 10)] for i in range(10)])

v3 = v1.dot(v2)

print("v1.dot(v2): ", v3)

v1 = Vector([[float(i)] for i in range(10)])
v2 = Vector([[float(i * 10)] for i in range(9)])

# v3 = v1.dot(v2) # should raise an error

# v3 = v1.dot(v2) # should raise an error


# transpose .T()

v1 = Vector([[float(i)] for i in range(10)])
v2 = Vector([[float(i * 10)] for i in range(9)])

print("v1: ", v1)
print("v1.T(): ", v1.T())

print("v2: ", v2)
print("v2.T(): ", v2.T())

# add and sub

v1 = Vector([[float(i)] for i in range(10)])
v2 = Vector([[float(i * 10)] for i in range(10)])

v3 = v1 + v2

print("v3 = v1 + v2: ", v3)

v3 = v2 - v1

print("v3 = v2 - v1: ", v3)

v1 = Vector([[float(i)] for i in range(10)])
v2 = Vector([[float(i * 10)] for i in range(9)])

# v3 = v1 + v2 # should raise an error

# v3 = v2 - v1 # should raise an error

# mul and rmul

v1 = Vector([[float(i)] for i in range(10)])
v2 = Vector([[float(i * 10)] for i in range(10)])

print("v1 * 2: ", v1 * 2)

print("2 * v1: ", 2 * v1)

# print("v1 * v2: ", v1 * v2) # should raise an error


# truediv and rtruediv

v1 = Vector([[float(i)] for i in range(10)])

print("v1 / 2: ", v1 / 2)

# print("2 / v1: ", 2 / v1) # should raise an error

# print("v1 / v1: ", v1 / v1) # should raise an error, other should be an int
