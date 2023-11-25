import math
import random
import typing as tp

import matplotlib.pyplot as plt

type Range = tp.Tuple[float, float]
Point = Range


def generate_random_point(x_range: Range, y_range: Range) -> Point:
    return random.uniform(*x_range), random.uniform(*y_range)


def is_in_circle(point: Point, center: Point, radius: float) -> bool:
    p_x, p_y = point
    c_x, c_y = center
    return (p_x - c_x) * (p_x - c_x) + (p_y - c_y) * (p_y - c_y) <= radius * radius
    

def estimate_pi(iterations: int) -> float:
    x_range = y_range = (-1, 1)
    generated_points = [generate_random_point(x_range, y_range) for _ in range(iterations)]
    return 4 * len([point for point in generated_points if is_in_circle(point, (0, 0), 1)]) / len(generated_points)


data_range = range(100, 5000 + 100, 100)
actual_approximation = [estimate_pi(n) for n in data_range]
relative_approximation = [100 * abs(approx - math.pi) / math.pi for approx in actual_approximation]

plt.scatter(data_range, actual_approximation)
plt.yticks(range(2, 6))
plt.axhline(y=math.pi, color="r", linestyle="-")
plt.xlabel("Iterantions")
plt.ylabel("PI approximation")
plt.show()

plt.scatter(data_range, relative_approximation)
plt.yticks(range(-1, 26))
plt.ylabel("% of deviation")
plt.axhline(y=0, color="r", linestyle="-")
plt.show()
