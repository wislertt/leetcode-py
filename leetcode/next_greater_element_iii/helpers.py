def run_next_greater_element(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.next_greater_element(n)


def assert_next_greater_element(result: int, expected: int) -> bool:
    assert result == expected
    return True
