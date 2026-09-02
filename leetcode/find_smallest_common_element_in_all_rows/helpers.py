def run_smallest_common_element(solution_class: type, mat: list[list[int]]):
    implementation = solution_class()
    return implementation.smallest_common_element(mat)


def assert_smallest_common_element(result: int, expected: int) -> bool:
    assert result == expected
    return True
