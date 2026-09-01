def run_maximum_element(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.maximum_element(arr)


def assert_maximum_element(result: int, expected: int) -> bool:
    assert result == expected
    return True
