def run_get_permutation(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.get_permutation(n, k)


def assert_get_permutation(result: str, expected: str) -> bool:
    assert result == expected
    return True
