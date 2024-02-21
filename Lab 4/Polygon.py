import math

def regular_polygon_area(num_sides, side_length):
    area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
    return area

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area_of_polygon = regular_polygon_area(num_sides, side_length)

print(f"The area of the polygon is: {area_of_polygon}")