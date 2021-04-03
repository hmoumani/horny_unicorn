from Vector import Vector

print("*" * 42)

v1 = Vector((13,37))

print(v1.values)
g = 5 + v1
print(g.values)
g = g + v1
print(g.values)

print("*" * 42)


v1 = Vector((13,37))

print(v1.values)
g = 5 - v1
print(g.values)
g = g - v1
print(g.values)


print("*" * 42)

v1 = Vector((13,37))
print(v1.values)
g = 13 / v1
print(g.values)

print("*" * 42)

v1 = Vector((13,37))
print(v1.values)
g = 2 * v1
print(g.values)
g = Vector(3) * Vector(3)
print(g)

print(str(v1))
print(repr(v1))