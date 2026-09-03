import random
from collections import Counter


def run_pick(
    solution_class: type, n: int, blacklist: list[int], seed: int, calls: int
) -> list[int]:
    random.seed(seed)
    implementation = solution_class(n, blacklist)
    return [implementation.pick() for _ in range(calls)]


def assert_pick(result: list[int], n: int, blacklist: list[int], calls: int) -> bool:
    black = set(blacklist)
    n_allowed = n - len(blacklist)
    assert len(result) == calls
    assert all(0 <= r < n and r not in black for r in result)
    if n_allowed <= 20 and n <= 10000 and calls >= 100 * n_allowed:
        allowed = {v for v in range(n) if v not in black}
        assert set(result) == allowed
    if calls >= 2000 and n_allowed <= 10 and n <= 10000:
        want = calls / n_allowed
        counts = Counter(result)
        lows = [v for v in range(n) if v not in black]
        assert all(0.5 * want <= counts[v] <= 1.5 * want for v in lows)
    return True
