def run_relative_sort_array(solution_class: type, arr1: list[int], arr2: list[int]):
    implementation = solution_class()
    return implementation.relative_sort_array(arr1, arr2)


def assert_relative_sort_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
