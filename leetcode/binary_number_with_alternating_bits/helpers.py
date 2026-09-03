def run_has_alternating_bits(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.has_alternating_bits(n)


def assert_has_alternating_bits(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
