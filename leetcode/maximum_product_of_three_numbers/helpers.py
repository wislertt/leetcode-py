def run_maximum_product(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.maximum_product(nums)


def assert_maximum_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
