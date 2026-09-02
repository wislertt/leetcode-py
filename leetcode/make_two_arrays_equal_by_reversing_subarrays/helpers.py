def run_can_be_equal(solution_class: type, target: list[int], arr: list[int]):
    implementation = solution_class()
    return implementation.can_be_equal(target, arr)


def assert_can_be_equal(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
