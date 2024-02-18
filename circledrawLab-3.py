import matplotlib.pyplot as plt

def bresenham_circle(x0, y0, radius):
  x = radius
  y = 0
  err = 0

  points = []

  while x >= y:
    points.append((x0 + x, y0 + y))
    points.append((x0 + y, y0 + x))
    points.append((x0 - y, y0 + x))
    points.append((x0 - x, y0 + y))
    points.append((x0 - x, y0 - y))
    points.append((x0 - y, y0 - x))
    points.append((x0 + y, y0 - x))
    points.append((x0 + x, y0 - y))

    y += 1
    err += 1 + 2*y
    if 2*(err-x) + 1 > 0:
      x -= 1
      err += 1 - 2*x

  return points
a = int(input("Enter the center coordinate of the circle (x and y): "))
b = a;
c = int(input("Enter the radius of the circle: "))
points = bresenham_circle(a, b, c);

# plot the points
plt.scatter([x for x, y in points], [y for x, y in points])

# draw the circle
circle = plt.Circle((a, b), c, fill=False)
plt.gcf().gca().add_artist(circle)

plt.show()