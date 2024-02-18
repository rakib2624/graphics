import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    """Implements Bresenham's Line Drawing Algorithm."""

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    p = 2 * dy - dx

    x, y = x1, y1

    points = []
    while x <= x2:
        points.append((x, y))

        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1

        x += 1

    plt.plot(*zip(*points))  # Plot the points using matplotlib
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Bresenham's Line Drawing Algorithm")
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
bresenham_line(x1, y1, x2, y2)