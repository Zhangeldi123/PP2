import math

def Volume_of_sphere(radius):
    if radius < 0:
        return "Radius should be non-negative."
    else:
        volume = (4/3) * math.pi * radius**3
        return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
result = Volume_of_sphere(radius)

if isinstance(result, str):
    print(result)
else:
    print(f"The volume of the sphere with radius {radius} is: {result:.2f}")