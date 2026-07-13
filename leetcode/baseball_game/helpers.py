def run_cal_points(solution_class: type, operations: list[str]):
    implementation = solution_class()
    return implementation.cal_points(operations)


def assert_cal_points(result: int, expected: int) -> bool:
    assert result == expected
    return True
