import matplotlib.pyplot as plt

def draw_circle_Bresenham(xc, yc, radius):
    x = 0
    y = radius
    d = 3 - 2 * radius
    
    points = []
    
    while x <= y:
        points.extend([(xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y),
                       (xc + y, yc + x), (xc - y, yc + x), (xc + y, yc - x), (xc - y, yc - x)])
        
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    
    return points

# Get input from the keyboard for circle's center and radius
xc = int(input("Enter the x-coordinate of the center: "))
yc = int(input("Enter the y-coordinate of the center: "))
radius = int(input("Enter the radius of the circle: "))

# Draw the circle using Bresenham's algorithm
points = draw_circle_Bresenham(xc, yc, radius)

# Plotting the circle
plt.figure()
plt.plot([point[0] for point in points], [point[1] for point in points], 'bo')
plt.title('Bresenham Circle Drawing Algorithm')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()