def run_transform_array(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.transform_array(arr)


def assert_transform_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
