def run_my_sqrt(solution_class: type, x: int):
    implementation = solution_class()
    return implementation.my_sqrt(x)


def assert_my_sqrt(result: int, expected: int) -> bool:
    assert result == expected
    return True
