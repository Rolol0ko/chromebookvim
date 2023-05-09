import math

def calculate():
    shape = input("Which shape? Circle (c), Rectangle (r), Square (s): ")
    shape = shape.lower()

    if  shape == "c":
        radius = input("Radius: ")
        radius = float(radius)
        Area = math.pi * (radius * radius)
        return Area
    elif shape == "r":
        length = input("Length: ")
        width = input("Width: ")
        Area = float(length) * float(width)
        return Area
    elif shape == "s":
        side = input("Side legth: ")
        Area = float(side) * float(side)
        return Area
    else:
        error = "Not a supported shape"
        return error

print(round(calculate(), 3))

