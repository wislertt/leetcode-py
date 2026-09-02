def run_get_modified_array(solution_class: type, length: int, updates: list[list[int]]):
    implementation = solution_class()
    return implementation.get_modified_array(length, updates)


def assert_get_modified_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
