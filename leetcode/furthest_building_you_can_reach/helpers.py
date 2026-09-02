def run_furthest_building(solution_class: type, heights: list[int], bricks: int, ladders: int):
    implementation = solution_class()
    return implementation.furthest_building(heights, bricks, ladders)


def assert_furthest_building(result: int, expected: int) -> bool:
    assert result == expected
    return True
