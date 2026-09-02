def run_count_elements(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.count_elements(arr)


def assert_count_elements(result: int, expected: int) -> bool:
    assert result == expected
    return True
