def run_is_strobogrammatic(solution_class: type, num: str):
    implementation = solution_class()
    return implementation.is_strobogrammatic(num)


def assert_is_strobogrammatic(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
