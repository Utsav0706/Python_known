class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Person deleted")


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"(X:{self.x}, Y:{self.y})"

    def __len__(self):
        return 200

    def __call__(self):
        print("Vector __call__")


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1+v2

print(v3)