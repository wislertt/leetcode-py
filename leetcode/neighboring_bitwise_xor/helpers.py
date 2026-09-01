def run_does_valid_array_exist(solution_class: type, derived: list[int]):
    implementation = solution_class()
    return implementation.does_valid_array_exist(derived)


def assert_does_valid_array_exist(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
