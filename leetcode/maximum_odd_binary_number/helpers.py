def run_maximum_odd_binary_number(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.maximum_odd_binary_number(s)


def assert_maximum_odd_binary_number(result: str, expected: str) -> bool:
    assert result == expected
    return True
