def run_most_booked(solution_class: type, n: int, meetings: list[list[int]]):
    implementation = solution_class()
    return implementation.most_booked(n, meetings)


def assert_most_booked(result: int, expected: int) -> bool:
    assert result == expected
    return True
