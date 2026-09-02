def run_longest_common_prefix(solution_class: type, arr1: list[int], arr2: list[int]):
    implementation = solution_class()
    return implementation.longest_common_prefix(arr1, arr2)


def assert_longest_common_prefix(result: int, expected: int) -> bool:
    assert result == expected
    return True
