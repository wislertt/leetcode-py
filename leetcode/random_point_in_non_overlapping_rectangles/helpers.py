import random


def run_pick(solution_class: type, rects: list[list[int]], seed: int, n: int) -> list[list[int]]:
    random.seed(seed)
    implementation = solution_class(rects)
    return [implementation.pick() for _ in range(n)]


def assert_pick(result: list[list[int]], rects: list[list[int]], n: int) -> bool:
    total = sum((x - a + 1) * (y - b + 1) for a, b, x, y in rects)
    assert result
    for u, v in result:
        assert any(a <= u <= x and b <= v <= y for a, b, x, y in rects)
    # Every integer point must be reachable, and each rectangle's share of the
    # draws must track its share of the integer points
    if n >= 2000 and total <= 40:
        assert len({(u, v) for u, v in result}) == total
        for a, b, x, y in rects:
            share = (x - a + 1) * (y - b + 1) / total
            got = sum(1 for u, v in result if a <= u <= x and b <= v <= y) / n
            assert abs(got - share) < 0.05
    return True
