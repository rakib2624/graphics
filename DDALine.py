import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    """Implements the DDA Line Drawing Algorithm."""

    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    points = []
    for i in range(int(steps + 1)):
        points.append((x, y))  # Collect points for visualization
        x += xinc
        y += yinc

    plt.plot(*zip(*points))  # Plot the points using matplotlib
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("DDA Line Drawing Algorithm")
    plt.grid(True)
    plt.show()

# Get input from keyboard
while True:
    try:
        x1 = int(input("Enter starting x-coordinate: "))
        y1 = int(input("Enter starting y-coordinate: "))
        x2 = int(input("Enter ending x-coordinate: "))
        y2 = int(input("Enter ending y-coordinate: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers.")

# Draw the line
dda_line(x1, y1, x2, y2)