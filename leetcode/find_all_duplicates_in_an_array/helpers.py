def run_find_duplicates(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_duplicates(nums)


def assert_find_duplicates(result: list[int], expected: list[int]) -> bool:
    # order of the duplicates does not matter
    assert sorted(result) == expected
    return True
