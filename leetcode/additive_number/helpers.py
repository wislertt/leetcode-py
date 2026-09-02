def run_is_additive_number(solution_class: type, num: str):
    implementation = solution_class()
    return implementation.is_additive_number(num)


def assert_is_additive_number(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
