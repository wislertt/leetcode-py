def run_k_inverse_pairs(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.k_inverse_pairs(n, k)


def assert_k_inverse_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
