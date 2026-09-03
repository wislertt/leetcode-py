def run_super_palindromes_in_range(solution_class: type, left: str, right: str):
    implementation = solution_class()
    return implementation.super_palindromes_in_range(left, right)


def assert_super_palindromes_in_range(result: int, expected: int) -> bool:
    assert result == expected
    return True
