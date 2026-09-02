def run_replace_elements(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.replace_elements(arr)


def assert_replace_elements(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
