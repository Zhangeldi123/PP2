import math

def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("Height: "))
base1_length = float(input("Base first value: "))
base2_length = float(input("Base second value: "))

area_of_trapezoid = trapezoid_area(height, base1_length, base2_length)

print(f"The area of the trapezoid is: {area_of_trapezoid}")