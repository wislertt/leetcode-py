def run_three_equal_parts(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.three_equal_parts(arr)


def assert_three_equal_parts(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
