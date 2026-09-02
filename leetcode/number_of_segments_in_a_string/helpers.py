def run_count_segments(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.count_segments(s)


def assert_count_segments(result: int, expected: int) -> bool:
    assert result == expected
    return True
