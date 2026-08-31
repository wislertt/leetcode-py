def assert_find_strobogrammatic_count(result: list[str], expected: int) -> bool:
    assert len(result) == expected
    return True


def run_find_strobogrammatic(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.find_strobogrammatic(n)


def assert_find_strobogrammatic(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
