def run_int_to_roman(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.int_to_roman(num)


def assert_int_to_roman(result: str, expected: str) -> bool:
    assert result == expected
    return True
