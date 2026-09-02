def run_binary_searchable_numbers(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.binary_searchable_numbers(nums)


def assert_binary_searchable_numbers(result: int, expected: int) -> bool:
    assert result == expected
    return True
