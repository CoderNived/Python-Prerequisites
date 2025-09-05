"""
Operator Overloading in Python
===============================
This file covers:
- Syntax of operator overloading
- Vector operations
- Complex number operations
- Comparison operators
- Extra examples for practical usage
"""

# -------------------------
# Example 1: Operator Overloading for Vectors
# -------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading -
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overloading *
    def __mul__(self, other):
        if isinstance(other, (int, float)):  # scalar multiplication
            return Vector(self.x * other, self.y * other)
        return Vector(self.x * other.x, self.y * other.y)

    # Overloading /
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return Vector(self.x / other.x, self.y / other.y)

    # Overloading ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading len() to return magnitude
    def __len__(self):
        from math import sqrt
        return int(sqrt(self.x ** 2 + self.y ** 2))

    # Overloading [] indexing
    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


print("\n--- Vector Operations ---")
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Multiplication:", v1 * v2)
print("Scalar Multiplication:", v1 * 3)
print("Division:", v2 / 2)
print("Equality:", v1 == v2)
print("Vector Magnitude (len):", len(v1))
print("First coordinate:", v1[0], "Second coordinate:", v1[1])

# -------------------------
# Example 2: Operator Overloading for Complex Numbers
# -------------------------

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"


print("\n--- Complex Number Operations ---")
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)

# -------------------------
# Example 3: Comparison Operators
# -------------------------

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other):  # less than
        return self.volume < other.volume

    def __gt__(self, other):  # greater than
        return self.volume > other.volume

    def __eq__(self, other):  # equality
        return self.volume == other.volume

    def __repr__(self):
        return f"Box(volume={self.volume})"


print("\n--- Comparison Operators ---")
b1 = Box(50)
b2 = Box(75)

print(f"{b1} < {b2} :", b1 < b2)
print(f"{b1} > {b2} :", b1 > b2)
print(f"{b1} == {b2} :", b1 == b2)

# -------------------------
# Example 4: Matrix Operator Overloading
# -------------------------

class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)


print("\n--- Matrix Addition ---")
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("Matrix 1:\n", m1)
print("Matrix 2:\n", m2)
print("Matrix 1 + Matrix 2:\n", m1 + m2)
