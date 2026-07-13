def run_permute_unique(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.permute_unique(nums)


def assert_permute_unique(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected])
    return True
