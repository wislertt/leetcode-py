def run_maximum_swap(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.maximum_swap(num)


def assert_maximum_swap(result: int, expected: int) -> bool:
    assert result == expected
    return True
