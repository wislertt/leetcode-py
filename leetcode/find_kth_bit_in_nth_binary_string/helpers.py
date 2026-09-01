def run_find_kth_bit(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.find_kth_bit(n, k)


def assert_find_kth_bit(result: str, expected: str) -> bool:
    assert result == expected
    return True
