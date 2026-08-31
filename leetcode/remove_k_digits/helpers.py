def run_remove_k_digits(solution_class: type, num: str, k: int):
    implementation = solution_class()
    return implementation.remove_k_digits(num, k)


def assert_remove_k_digits(result: str, expected: str) -> bool:
    assert result == expected
    return True
