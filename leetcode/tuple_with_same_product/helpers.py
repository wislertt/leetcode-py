def run_tuple_same_product(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.tuple_same_product(nums)


def assert_tuple_same_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
