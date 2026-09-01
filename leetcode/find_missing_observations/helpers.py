def run_missing_rolls(solution_class: type, rolls: list[int], mean: int, n: int):
    implementation = solution_class()
    return implementation.missing_rolls(rolls, mean, n)


def assert_missing_rolls(result: list[int], expected: list[int]) -> bool:
    # Multiple valid answers exist; verify length, dice range and sum
    # instead of exact equality
    assert len(result) == len(expected)
    assert all(1 <= roll <= 6 for roll in result)
    assert sum(result) == sum(expected)
    return True
