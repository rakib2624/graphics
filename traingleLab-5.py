import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

def rotate_point(point, center, angle):
    """
    Rotate a point around another point by a given angle.
    
    Parameters:
        point: tuple, coordinates of the point to rotate (x, y).
        center: tuple, coordinates of the center of rotation (x, y).
        angle: float, angle of rotation in degrees.
    
    Returns:
        rotated_point: tuple, coordinates of the rotated point (x, y).
    """
    # Convert angle to radians
    angle_rad = radians(angle)
    
    # Translate the point to the origin
    translated_point = (point[0] - center[0], point[1] - center[1])
    
    # Perform the rotation
    rotated_point = (translated_point[0] * cos(angle_rad) - translated_point[1] * sin(angle_rad) + center[0],
                     translated_point[0] * sin(angle_rad) + translated_point[1] * cos(angle_rad) + center[1])
    
    return rotated_point

# Function to draw a triangle
def draw_triangle(triangle_points):
    triangle_points.append(triangle_points[0])  # Close the triangle
    x_coords = [point[0] for point in triangle_points]
    y_coords = [point[1] for point in triangle_points]
    plt.plot(x_coords, y_coords, 'b-')

# Get input from the keyboard for triangle vertices
print("Enter coordinates of the triangle vertices (x, y) separated by spaces:")
triangle_points = []
for _ in range(3):
    x, y = map(int, input().split())
    triangle_points.append((x, y))

# Plot the original triangle
plt.figure()
draw_triangle(triangle_points)
plt.title('Original Triangle')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Get input from the keyboard for the rotation point and angle
center_x, center_y = map(int, input("Enter coordinates of the center of rotation (x, y): ").split())
angle = float(input("Enter the angle of rotation in degrees: "))

# Rotate each vertex of the triangle around the rotation point
rotated_triangle_points = [rotate_point(point, (center_x, center_y), angle) for point in triangle_points]

# Plot the rotated triangle
draw_triangle(rotated_triangle_points)
plt.title('Rotated Triangle')
plt.show()