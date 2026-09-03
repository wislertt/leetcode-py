def run_find_kth_number(solution_class: type, m: int, n: int, k: int):
    implementation = solution_class()
    return implementation.find_kth_number(m, n, k)


def assert_find_kth_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
