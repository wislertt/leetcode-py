def run_sort_jumbled(solution_class: type, mapping: list[int], nums: list[int]):
    implementation = solution_class()
    return implementation.sort_jumbled(mapping, nums)


def assert_sort_jumbled(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
