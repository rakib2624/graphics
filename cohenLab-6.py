import matplotlib.pyplot as plt

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to calculate region code for a point
def calculate_region_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

# Function to clip a line using Cohen-Sutherland algorithm
def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = calculate_region_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = calculate_region_code(x2, y2, xmin, ymin, xmax, ymax)
    
    while (code1 | code2) != 0:
        if (code1 & code2) != 0:
            return None, None, None, None  # Both points are outside the clipping window
        
        # Choose a point outside the clipping window
        code = code1 if code1 != 0 else code2
        
        # Calculate intersection point
        if code & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif code & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif code & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif code & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        
        # Update the intersection point and region code
        if code == code1:
            x1, y1 = x, y
            code1 = calculate_region_code(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            code2 = calculate_region_code(x2, y2, xmin, ymin, xmax, ymax)
    
    return x1, y1, x2, y2

# Function to plot a line segment
def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], 'b-')

# Get input from the keyboard for line coordinates and clipping window
x1, y1 = map(int, input("Enter the coordinates of the first point of the line (x1 y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of the second point of the line (x2 y2): ").split())
xmin, ymin, xmax, ymax = map(int, input("Enter the coordinates of the clipping window (xmin ymin xmax ymax): ").split())

# Clip the line using Cohen-Sutherland algorithm
x1_clip, y1_clip, x2_clip, y2_clip = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

# Plot the original line
plt.figure()
draw_line(x1, y1, x2, y2)

# Plot the clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r--', label='Clipping Window')

# Plot the clipped line (if it exists)
if x1_clip is not None:
    draw_line(x1_clip, y1_clip, x2_clip, y2_clip)
    plt.title('Cohen-Sutherland Line Clipping Algorithm (Clipped)')
else:
    plt.title('Cohen-Sutherland Line Clipping Algorithm (No Intersection)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
