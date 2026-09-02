import random


def run_rand_point(
    solution_class: type, radius: float, x_center: float, y_center: float, seed: int, n: int
) -> list[list[float]]:
    random.seed(seed)
    implementation = solution_class(radius, x_center, y_center)
    return [implementation.rand_point() for _ in range(n)]


def assert_rand_point(
    result: list[list[float]], radius: float, x_center: float, y_center: float, n: int
) -> bool:
    limit = radius * radius + 1e-9
    assert result
    for x, y in result:
        assert (x - x_center) ** 2 + (y - y_center) ** 2 <= limit
    # Uniform sampling over enough draws covers all four quadrants
    if n >= 200:
        quadrants = {(x >= x_center, y >= y_center) for x, y in result}
        assert len(quadrants) == 4
    # The inner half-radius disk holds a quarter of the area
    if n >= 2000:
        inner = sum(1 for x, y in result if (x - x_center) ** 2 + (y - y_center) ** 2 <= limit / 4)
        assert abs(inner / n - 0.25) < 0.05
    return True
