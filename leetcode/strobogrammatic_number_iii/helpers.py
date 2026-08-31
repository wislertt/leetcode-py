def run_strobogrammatic_in_range(solution_class: type, low: str, high: str):
    implementation = solution_class()
    return implementation.strobogrammatic_in_range(low, high)


def assert_strobogrammatic_in_range(result: int, expected: int) -> bool:
    assert result == expected
    return True
