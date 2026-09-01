def run_paint_walls(solution_class: type, cost: list[int], time: list[int]):
    implementation = solution_class()
    return implementation.paint_walls(cost, time)


def assert_paint_walls(result: int, expected: int) -> bool:
    assert result == expected
    return True
