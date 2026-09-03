def run_hit_bricks(solution_class: type, grid: list[list[int]], hits: list[list[int]]):
    implementation = solution_class()
    return implementation.hit_bricks(grid, hits)


def assert_hit_bricks(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
