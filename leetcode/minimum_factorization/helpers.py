def run_smallest_factorization(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.smallest_factorization(num)


def assert_smallest_factorization(result: int, expected: int) -> bool:
    assert result == expected
    return True
