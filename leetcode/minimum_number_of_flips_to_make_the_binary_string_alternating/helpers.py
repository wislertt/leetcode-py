def run_min_flips(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.min_flips(s)


def assert_min_flips(result: int, expected: int) -> bool:
    assert result == expected
    return True
