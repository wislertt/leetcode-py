def run_smallest_number(solution_class: type, pattern: str):
    implementation = solution_class()
    return implementation.smallest_number(pattern)


def assert_smallest_number(result: str, expected: str) -> bool:
    assert result == expected
    return True
