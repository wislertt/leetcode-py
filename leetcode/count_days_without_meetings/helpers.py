def run_count_days(solution_class: type, days: int, meetings: list[list[int]]):
    implementation = solution_class()
    return implementation.count_days(days, meetings)


def assert_count_days(result: int, expected: int) -> bool:
    assert result == expected
    return True
