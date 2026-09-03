def run_can_reorder_doubled(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.can_reorder_doubled(arr)


def assert_can_reorder_doubled(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
