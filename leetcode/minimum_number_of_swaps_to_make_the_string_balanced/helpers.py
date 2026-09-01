def run_min_swaps(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_swaps(s)


def assert_min_swaps(result: int, expected: int) -> bool:
    assert result == expected
    return True
