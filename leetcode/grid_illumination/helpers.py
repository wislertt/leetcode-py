def run_grid_illumination(
    solution_class: type, n: int, lamps: list[list[int]], queries: list[list[int]]
):
    implementation = solution_class()
    return implementation.grid_illumination(n, lamps, queries)


def assert_grid_illumination(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
